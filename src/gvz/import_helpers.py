"""
Import helper functions for CSV files
"""

import csv
from .models import AdministrativeDivision, ZipCode

def generate_ags_id(row):
    """
    Concatenate id columns to the AGS ID.
    """
    if row[0] == "50":
        return "{}{}{}{}".format(row[2], row[3], row[4], row[5])
    return "{}{}{}{}".format(row[2], row[3], row[4], row[6])

def get_parent_division(row):
    """
    Calculate the parent AGS ID for a given row. Set the last AGS column to empty string.
    Repeat setting the last AGS columnt to empty string, until it matches an existing entry.
    This match is then expected to be the correct parent.
    """
    index = 5
    for number in range(5, 1, -1):
        if row[number] != "":
            index = number - 1
            row[number] = ""
            break
    while index >= 2:
        ags = "{}{}{}{}".format(row[2], row[3], row[4], row[5])
        parent = AdministrativeDivision.objects.filter(ags=ags).first()
        if parent:
            return parent
        row[index] = ""
        index = index - 1
    return None

def import_gvz_data(csv_file):
    """
    Import "Gemeindeverzeichnis" CSV file. This is the Excel file provided by
    destatis.de where the header lines are reduced to one row.

    Columns:
        # 0 Satzart
        # 1 Textkennzeichen
        # 2 Land
        # 3 RB
        # 4 Kreis
        # 5 VB
        # 6 Gem
        # 7 Gemeindename
        # 8 Fläche
        # 9 Bevölkerung
        # 10 männlich
        # 11 weiblich
        # 12 Bevölkerungsdichte
        # 13 Postleitzahl
        # 14 Längengrad
        # 15 Breitengrad
        # 16 Reisegebiete
        # 17 Reisegebietbezeichnung
        # 18 Besiedlung Schlüssel
        # 19 Besiedlung Bezeichnung
    """
    reader = csv.reader(csv_file.splitlines(), delimiter=';')
    next(reader) # skip header
    for row in reader:
        ags = generate_ags_id(row)
        ad_di = AdministrativeDivision.objects.get_or_create(ags=ags)[0]
        ad_di.name = row[7]
        parent_ags = get_parent_division(row)
        if parent_ags:
            ad_di.parent = parent_ags
        else:
            ad_di.parent = None
        ad_di.division_category = row[0]
        ad_di.division_type = row[1] if row[1] != "" else row[0]
        ad_di.office_zip = int(row[13]) if row[13] else None
        ad_di.office_street = ""
        ad_di.office_city = ""
        ad_di.area = float(row[8].replace(',', '.')) if row[8] else None
        ad_di.citizens_total = int(row[9].replace(' ', '')) if row[9] else None
        ad_di.citizens_female = int(row[10].replace(' ', '')) if row[10] else None
        ad_di.citizens_male = int(
            row[11].replace(' ', '')) if row[11] else None
        ad_di.population_density = float(
            row[12].replace(',', '.').replace(' ', '')) if row[12] else None
        ad_di.longitude = float(row[14].replace(',', '.').replace(' ', '')) if row[14] else None
        ad_di.latitude = float(row[15].replace(',', '.').replace(' ', '')) if row[15] else None
        ad_di.travel_code = row[16] if row[16] else None
        ad_di.travel_name = row[17] if row[17] else None
        ad_di.save()

def import_zip_data(csv_file):
    """
    Import zip codes from a CSV file provided by https://www.suche-postleitzahl.org/downloads

    Columns: osm_id,ags,ort,plz,landkreis,bundesland
    """
    reader = csv.reader(csv_file.splitlines(), delimiter=',')
    next(reader)
    for row in reader:
        ad_di = AdministrativeDivision.objects.filter(ags=row[1]).first()
        if ad_di:
            zip_code = ZipCode.objects.get_or_create(
                zip_code=row[3], administrative_division=ad_di)[0]
            zip_code.save()
