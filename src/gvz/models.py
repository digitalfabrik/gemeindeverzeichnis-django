"""
Model for municipalities and zip codes
"""
from django.db import models

from .constants import ADMINISTRATIVE_TYPES

class AdministrativeDivision(models.Model):
    """
    GVZ line (administrative division)
    """
    ags = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    division_category = models.IntegerField()
    division_type = models.CharField(max_length=64, choices=ADMINISTRATIVE_TYPES)
    office_zip = models.IntegerField(blank=True)
    office_street = models.CharField(max_length=255, blank=True)
    office_city = models.CharField(max_length=255, blank=True)
    area = models.FloatField(blank=True)
    citizens_total = models.IntegerField(blank=True)
    citizens_female = models.IntegerField(blank=True)
    citizens_male = models.IntegerField(blank=True)
    population_density = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
    TRAVEL_CODE = models.CharField(max_length=4, blank=True)
    TRAVLE_NAME = models.CharField(max_length=128, blank=True)

class ZipCode(models.Model):
    """
    zip codes for administrative divisions
    """
    zip_code = models.IntegerField()
    administrative_division = models.ForeignKey(AdministrativeDivision, on_delete=models.CASCADE)
