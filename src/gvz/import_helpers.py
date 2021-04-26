"""
Import helper functions for CSV files and statistikportal.de crawler
"""

from io import StringIO
import csv
import requests
from lxml import etree

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
    for number in range(6, 1, -1):
        if row[number] != "":
            index = number
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
        ad_di = AdministrativeDivision.objects.get_or_create(
            ags=ags,
            division_category=int(row[0]),
            division_type=int(row[1]) if row[1] != "" else int(row[0])
        )[0]
        ad_di.name = row[7]
        parent_ags = get_parent_division(row)
        if parent_ags:
            ad_di.parent = parent_ags
        else:
            ad_di.parent = None
        ad_di.office_zip = row[13] if row[13] else None
        ad_di.office_street = None
        ad_di.office_city = None
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

def crawl_contact_address(ags):
    """
    Send request to statistikportal.de
    """
    url = 'https://www.statistikportal.de/de/gemeindeverzeichnis?ajax_form=1&_wrapper_format=drupal_ajax'
    payload = {'mi_search': str(ags), 'form_id': 'municipality_index_search'}
    response = requests.post(url, data=payload).json()
    html = response[0]["data"]
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    previous = ""
    result = {"office_zip": "", "office_street": "", "office_city": "", "office_name": ""}

    for item in tree.findall('.//div'):
        text = item.text.strip(' \t\n\r')
        if text != "":
            if previous == "Anschrift der Gemeinde":
                result["office_name"] = text
            elif previous == "Straße":
                result["office_street"] = text
            elif previous == "Ort":
                str_list = list(filter(None, text.split(" ")))
                result["office_zip"] = str_list[0]
                result["office_city"] = str_list[1]
            previous = text
    return result
