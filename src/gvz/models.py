"""
Model for municipalities and zip codes
"""
from django.db import models

from .constants import ADMINISTRATIVE_TYPES

class AdministrativeDivision(models.Model):
    """
    GVZ line (administrative division)
    """
    ags = models.CharField(unique=True, max_length=9)
    name = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    division_category = models.IntegerField(blank=True, null=True)
    division_type = models.CharField(max_length=64, choices=ADMINISTRATIVE_TYPES)
    office_zip = models.IntegerField(blank=True, null=True)
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

    def __str__(self):
        #if self.parent:
        #    return str(self.parent) + " > (" + self.ags + ") " + self.name
        return self.name + " (AGS: " + self.ags + " " + self.get_division_type_display() + ") "



class ZipCode(models.Model):
    """
    zip codes for administrative divisions
    """
    zip_code = models.IntegerField()
    administrative_division = models.ForeignKey(AdministrativeDivision, on_delete=models.CASCADE)
