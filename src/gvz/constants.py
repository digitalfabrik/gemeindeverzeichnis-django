"""
German administrative divions
"""
# Bundesland
STATE = 10
# Regierungsbezirk
ADMINISTRATIVE_DISTRICT = 20
# Region
REGION = 30
# Kreis
CT_ABSTRACT = 40
# Kreisfreie Stadt
CT_URBAN_MUNICIPALITY = 41
# Stadtkreis
CT_METROPOLITAN_AREA = 42
# Kreis
CT_COUNTY = 43
# Landkreis
CT_RURAL_COUNTY = 44
# Regionalverband
CT_COLLECTIVE_COUNTY = 45
# verbandsfreie Gemeinde
MU_UNASSOCIATED_MUNICIPALITY = 50
# Amt
MU_OFFICE = 51
# Samtgemeinde
MU_JOINT_COMMUNITY = 52
# Verbandsgemeinde
MU_COLLECTIVE_MUNICIPALITY = 53
# Verwaltungsgemeinschaft
MU_ADMINISTRATIVE_COLLECTIVITY = 54
# Kirchspielslandgemeinde
MU_CHURCH_COMMUNITY = 55
# Verwaltungsverband
MU_ADMINISTRATIVE_UNION = 56
# VG Trägermodell
MU_COLLECTIVE_MUNICIPALITY_MODEL = 57
# Erfüllgende Gemeinde
MU_EXECUTING_MUNICIPALITY = 58
# Markt
MP_MARKET = 60
# Kreisfreie Stadt
MP_URBAN_MUNICIPALITY = 61
# Stadtkreis
MP_METROPOLITAN_AREA = 62
# Stadt
MP_CITY = 63
# Kreisangehörige Gemeinde
MP_ASSOCIATED_MUNICIPALITY = 64
# gemeindefreies Gebiet, bewohnt
MP_UNASSOCIATED_AREA_INHABITED = 65
# gemeindefreies Gebiet, unbewohnt
MP_UNASSOCIATED_AREA_UNINHABITED = 66
# große Kreisstadt
MP_LARGE_CITY = 67

ADMINISTRATIVE_TYPES = [
    (STATE, 'Bundesland'),
    (ADMINISTRATIVE_DISTRICT, 'Regierungsbezirk'),
    (REGION, 'Region'),
    (CT_ABSTRACT, 'Kreis'),
    (CT_URBAN_MUNICIPALITY, 'Kreisfreie Stadt'),
    (CT_METROPOLITAN_AREA, 'Stadtkreis'),
    (CT_COUNTY, 'Kreis'),
    (CT_RURAL_COUNTY, 'Landkreis'),
    (CT_COLLECTIVE_COUNTY, 'Regionalverband'),
    (MU_UNASSOCIATED_MUNICIPALITY, 'verbandsfreie Gemeinde'),
    (MU_OFFICE, 'Amt'),
    (MU_JOINT_COMMUNITY, 'Samtgemeinde'),
    (MU_COLLECTIVE_MUNICIPALITY, 'Verbandsgemeinde'),
    (MU_ADMINISTRATIVE_COLLECTIVITY, 'Verwaltungsgemeinschaft'),
    (MU_CHURCH_COMMUNITY, 'Kirchspielslandgemeinde'),
    (MU_ADMINISTRATIVE_UNION, 'Verwaltungsverband'),
    (MU_COLLECTIVE_MUNICIPALITY_MODEL, 'VG Trägermodell'),
    (MU_EXECUTING_MUNICIPALITY, 'Erfüllende Gemeinde'),
    (MP_MARKET, 'Markt'),
    (MP_URBAN_MUNICIPALITY, 'Kreisfreie Stadt'),
    (MP_METROPOLITAN_AREA, 'Stadtkreis'),
    (MP_CITY, 'Stadt'),
    (MP_ASSOCIATED_MUNICIPALITY, 'Kreisangehörige Gemeinde'),
    (MP_UNASSOCIATED_AREA_INHABITED, 'gemeindefreies Gebiet, bewohnt'),
    (MP_UNASSOCIATED_AREA_UNINHABITED, 'gemeindefreies Gebiet, unbewohnt'),
    (MP_LARGE_CITY, 'große Kreisstadt'),
]
