"""
Django admin back end
"""
# pylint: disable=R0903

from django.db.models import Q
from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.urls import path

from .models import AdministrativeDivision, ZipCode
from .import_helpers import import_gvz_data, import_zip_data, crawl_contact_address

class CsvImportForm(forms.Form):
    """
    Simple form to add CSV button
    """
    csv_file = forms.FileField()

@admin.register(AdministrativeDivision)
class AdministrativeDivisionAdmin(admin.ModelAdmin):
    """
    Extend AdministrativeDivision with CSV import functionality
    """
    change_list_template = "admin/administrative_division_changelist.html"

    def get_urls(self):
        """
        Extend URLs list with import path
        """
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
            path('crawl-contact-addresses/', self.crawl_contact_addresses)
        ]
        return my_urls + urls

    def import_csv(self, request):
        """
        Handle CSV form requests
        """
        if request.method == "POST":
            import_gvz_data(request.FILES["csv_file"].read().decode())
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

    def crawl_contact_addresses(self, request):
        """
        Contact statisticportal.de API and extract contact information
        """
        payload = {"updated": []}
        divisions = AdministrativeDivision.objects.filter(
            (Q(office_street=None) | Q(office_city=None) | Q(office_zip=None)) &
            Q(division_type=60))
        for division in divisions[:100]:
            result = crawl_contact_address(division.ags)
            division.office_street = result["office_street"]
            division.office_city = result["office_city"]
            division.office_name = result["office_name"]
            division.save()
            payload["updated"].append(division.ags)
        return render(
            request, "admin/crawled_list.html", payload
        )

@admin.register(ZipCode)
class ZipCodeAdmin(admin.ModelAdmin):
    """
    Extend ZipCodes admin with CSV import functionality
    """
    change_list_template = "admin/administrative_division_changelist.html"

    def get_urls(self):
        """
        Extend URLs with CSV import path
        """
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        """
        Handle CSV import requests
        """
        if request.method == "POST":
            import_zip_data(request.FILES["csv_file"].read().decode())
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
