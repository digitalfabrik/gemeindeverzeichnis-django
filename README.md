# Digitalfabrik Gemeindeverzeichnis
Dies ist ein Dienst, welcher in einer API die Informationen aus dem Gemeindeverzeichnis in einer API bereitstellt. Zusätzlich werden die Gemeindedaten mit Postleitzahlen angereichert.

In diesem Verzeichnis sind die hierarchischen Informationen erhalten.

# Quellen
* [Excel Datei des Gemeindeverzeichnis](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html)
* [Zuordnung Postleitzahlen und Landkreise](https://www.suche-postleitzahl.org/download_files/public/zuordnung_plz_ort_landkreis.csv)

# API Dokumentation
Die [API](https://gvz.tuerantuer.org/api/) kann direkt im Browser durchsucht werden. Es gibt zwei verschiedene Models, die durchsucht werden können:
* [Administrative Einheiten](https://gvz.tuerantuer.org/api/administrative_divisions/)
* [Postleitzahlen](https://gvz.tuerantuer.org/api/zip_codes/)

Rechts oben befindet sich ein "Filter" Button, über den nach verschiedenen Attributen gefiltert werden kann.

## Suche nach Postleitzahl oder Name
Die API unterstützt die Suche direkt nach Ortsnamen oder Postleitzahlen:
* [https://gvz.tuerantuer.org/api/administrative_divisions/?search=Augsburg](https://gvz.tuerantuer.org/api/administrative_divisions/?search=Augsburg)
* [https://gvz.tuerantuer.org/api/administrative_divisions/?search=86150](https://gvz.tuerantuer.org/api/administrative_divisions/?search=86150)

## Filter nach Kategorie
Um beispielsweise nur Objekte der Kategorie Bundesland anzuzeigen, kann folgender Filter genutzt werden:
* [https://gvz.tuerantuer.org/api/administrative_divisions/?division_category=10](https://gvz.tuerantuer.org/api/administrative_divisions/?division_category=10)

## Felder
* `id`: Datenbank-ID, findet Verwendung in Pfaden zu Objekten
* `ags`: offizieller Gemeindeschlüssel
* `name`: Name der Gemeinde, Kreis, Land, etc
* `division_category`: Kategorie-ID (Bundesland, Regierungsbezirk, Region, Kreis, Gemeindeverband, Gemeinde)
* `division_category_name`: Kategorie-Name der regionalen Einheit
* `division_type`: Offizieller Kennziffer/Bezeichner für die regionale Einheit (Markt, Samtgemeinde, etc)
* `division_type_name`: Bezeichnung des Typs der regionale Einheit
* `office_zip`: Postleitzahl der Anschrift
* `office_street`: Straße der Anschrift
* `office_city`: Stadt der Anschrift
* `area`: Offizielle Angabe Fläche in km²
* `citizens_total`: Offizielle Angabe Einwohner:innen
* `citizens_male`: Offizielle Angabe männliche Einwohner
* `citizens_female`: Offizielle weibliche Einwohnerinnen
* `area_accumulated`: berechnete Summe der Fläche aller untergeordneten Einheiten
* `citizens_accumulated`: berechnete Summe der Einwohner:innen der untergeordneten Einheiten
* `population_density`: Bevölkerungsdichte pro Quadratkilometer
* `longitude`: Längengrad
* `latitude`: Breitengrad
* `travel_name`: Reisegebietsname
* `travel_code`: Reisegebietskennziffer
* `url`: Pfad zum Object
* `parent`: Pfad zum übergeordneten Projekt
* `children`: Liste der Pfade zu untergeordneten Objekten
* `zip_codes`: Liste aller untergeordneter Postleitzahlen

Folgende Felder können zum Filtern genutzt werden:
* Gemeindeschlüssel
* Kategorie (Ebene) der regionalen Einheit (Land, Regierungsbezirk, Kreis, etc)
* Name
* Datenbank-ID der Übergeordneten regionale Einheit

## Kennzeichen für regionale Einheiten und Kategorien
### Kategorien (Destatis Satzart)
* 10=Land
* 20=Regierungsbezirk
* 30=Region (nur in Baden-Württemberg)
* 40=Kreis
* 50=Gemeindeverband
* 60=Gemeinde

### regionale Einheiten (Destatis Textkennzeichen)
* 41=Kreisfreie Stadt
* 42=Stadtkreis (nur in Baden-Württemberg)
* 43=Kreis
* 44=Landkreis
* 45=Regionalverband (nur im Saarland)
* 50=Verbandsfreie Gemeinde
* 51=Amt
* 52=Samtgemeinde
* 53=Verbandsgemeinde
* 54=Verwaltungsgemeinschaft
* 55=Kirchspielslandgemeinde
* 56=Verwaltungsverband
* 58=Erfüllende Gemeinde
* 60=Markt
* 61=Kreisfreie Stadt
* 62=Stadtkreis (nur in Baden-Württemberg)
* 63=Stadt
* 64=Kreisangehörige Gemeinde
* 65=gemeindefreies Gebiet-bewohnt
* 66=gemeindefreies Gebiet-unbewohnt
* 67=Große Kreisstadt

# Lizenz
Der Quellcode ist [Apache 2.0](LICENSE.txt) lizenziert.
