"""
Model for municipalities and zip codes
"""
# pylint: disable=R0903

from django.db import models

from .constants import DIVISION_CATEGORIES, ADMINISTRATIVE_TYPES


class AdministrativeDivision(models.Model):
    """
    GVZ line (administrative division)
    """
    ags = models.CharField(unique=True, max_length=9)
    name = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.CASCADE, related_name="children")
    division_category = models.IntegerField(choices=DIVISION_CATEGORIES)
    division_type = models.IntegerField(choices=ADMINISTRATIVE_TYPES)
    office_name = models.CharField(max_length=128, blank=True, null=True)
    office_zip = models.CharField(max_length=5, blank=True, null=True)
    office_street = models.CharField(max_length=255, blank=True, null=True)
    office_city = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    citizens_total = models.IntegerField(blank=True, null=True)
    citizens_female = models.IntegerField(blank=True, null=True)
    citizens_male = models.IntegerField(blank=True, null=True)
    population_density = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    travel_code = models.CharField(max_length=4, blank=True, null=True)
    travel_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        """
        Django model meta information
        """
        indexes = [
            models.Index(fields=['ags',]),
            models.Index(fields=['division_type',]),
            models.Index(fields=['division_category',]),
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        category = self.get_division_category_display()
        if category is None:
            category = ""
        return (self.name + " (AGS: " + self.ags + ", Kategorie: " +
                category + ") ")

    @property
    def zip_codes(self):
        """
        Return zip codes
        """
        zip_codes = []
        for child in AdministrativeDivision.objects.filter(parent=self):
            zip_codes = zip_codes + child.zip_codes
        zip_codes = (zip_codes +
                     [item.zip_code for item in
                      ZipCode.objects.filter(administrative_division=self)])
        return zip_codes

    @property
    def division_category_name(self):
        """
        Return display name of division category
        """
        return self.get_division_category_display()

    @property
    def division_type_name(self):
        """
        Return display name of division type
        """
        return self.get_division_type_display()

    @property
    def citizens_accumulated(self):
        """
        Sum up population of children
        """
        if self.division_category == 60:
            return {"total": self.citizens_total,
                    "female": self.citizens_female,
                    "male": self.citizens_male}

        accumulated = {
            "total": 0,
            "female": 0,
            "male": 0
        }
        for child in AdministrativeDivision.objects.filter(parent=self):
            child_citizens = child.citizens_accumulated
            accumulated["total"] = accumulated["total"] + child_citizens["total"]
            accumulated["female"] = accumulated["female"] + child_citizens["female"]
            accumulated["male"] = accumulated["male"] + child_citizens["male"]
        return accumulated

    @property
    def area_accumulated(self):
        """
        Sum up area of children
        """
        if self.division_category == 60:
            return self.area
        accumulated_area = 0
        for child in AdministrativeDivision.objects.filter(parent=self):
            accumulated_area = accumulated_area + child.area_accumulated
        return accumulated_area

class ZipCode(models.Model):
    """
    zip codes for administrative divisions
    """
    zip_code = models.CharField(max_length=5)
    administrative_division = models.ForeignKey(AdministrativeDivision,
                                                on_delete=models.CASCADE,
                                                related_name="zip_codes_objects")

    class Meta:
        """
        Django model meta information
        """
        unique_together = ('zip_code', 'administrative_division',)
        indexes = [
            models.Index(fields=['zip_code',]),
        ]

    def __str__(self):
        return str(self.zip_code) + ": " + str(self.administrative_division)
