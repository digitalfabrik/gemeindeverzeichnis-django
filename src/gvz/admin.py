from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.urls import path

from .models import AdministrativeDivision, ZipCode

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(AdministrativeDivision)
class AdministrativeDivisionAdmin(admin.ModelAdmin):
    change_list_template = "admin/administrative_division_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            #reader = csv.reader(csv_file)
            # Create Hero objects from passed in data
            # ...
            #self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )


@admin.register(ZipCode)
class ZipCodeAdmin(admin.ModelAdmin):
    change_list_template = "admin/administrative_division_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            #reader = csv.reader(csv_file)
            # Create Hero objects from passed in data
            # ...
            #self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )
