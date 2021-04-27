# Digitalfabrik Gemeindeverzeichnis
Dieser Dienst stellt Informationen aus dem [Gemeindeverzeichnis des statistischen Bundesamts](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html) in einer grafischen Oberfläche sowie API bereit. Zusätzlich werden die Gemeindedaten mit Postleitzahlen aus [suche-postleitzahl.org](https://suche-postleitzahl.org) angreichert.

In diesem Verzeichnis sind die hierarchischen Informationen enthalten. Bevölkerungzahl, Fläche und Postleitzahlen werden aus untergeordneten Einheiten zusammengeführt.

Eine einfache grafische Oberfläche des Verzeichnisses ist auf [https://gvz.tuerantuer.org](https://gvz.tuerantuer.org) nutzbar. Über die grafisch aufbereitete [API](#api-dokumentation) stehen alle Informationen zur Verfügung.

# Quellen
* [Excel Datei des Gemeindeverzeichnis](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html)
* [Zuordnung Postleitzahlen und Landkreise](https://www.suche-postleitzahl.org/download_files/public/zuordnung_plz_ort_landkreis.csv)
* [Anschriften der Gemeinden](https://www.statistikportal.de/de/gemeindeverzeichnis)

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
* `division_category`: Kennziffer der Kategorie der regionalen Einheit (Ebene)
* `division_category_name`: Kategorie-Name der regionalen Einheit
* `division_type`: Kennziffer des Typs der regionalen Einheit (Stadt, Markt, Samtgemeinde, etc)
* `division_type_name`: Name des Typs der regionale Einheit
* `office_name`: Anschrift (Name) (1)
* `office_zip`: Postleitzahl der Anschrift (1)
* `office_street`: Straße der Anschrift (1)
* `office_city`: Stadt der Anschrift (1)
* `area`: Offizielle Angabe Fläche in km² (1)
* `citizens_total`: Offizielle Angabe Einwohner:innen (1)
* `citizens_male`: Offizielle Angabe männliche Einwohner (1)
* `citizens_female`: Offizielle weibliche Einwohnerinnen (1)
* `area_accumulated`: berechnete Summe der Fläche aller untergeordneten Einheiten
* `citizens_accumulated`: berechnete Summe der Einwohner:innen der untergeordneten Einheiten
* `population_density`: Bevölkerungsdichte pro Quadratkilometer (1)
* `longitude`: Längengrad (1)
* `latitude`: Breitengrad (1)
* `travel_name`: Reisegebietsname (1)
* `travel_code`: Reisegebietskennziffer (1)
* `url`: Pfad zum Object
* `parent`: Pfad zum übergeordneten Projekt
* `children`: Liste der Pfade zu untergeordneten Objekten
* `zip_codes`: Liste aller untergeordneter Postleitzahlen

Anmerkung: 1) nur für Gemeinden verfügbar

Folgende Felder können zum Filtern genutzt werden:
* Gemeindeschlüssel (`ags`)
* Kategorie (Ebene) der regionalen Einheit (Land, Regierungsbezirk, Kreis, etc) (`division_category`)
* Typ der regionalen Einheit (`division_type`)
* Name (`name`)
* Datenbank-ID der Übergeordneten regionale Einheit (`id`)

## Kennziffern für regionale Einheiten
### Kategorien (Destatis "Satzart")
* 10=Land
* 20=Regierungsbezirk
* 30=Region (nur in Baden-Württemberg)
* 40=Kreis
* 50=Gemeindeverband
* 60=Gemeinde

### Typenbezeichnung (Destatis "Textkennzeichen")
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

# Installation
1. Repository klonen
2. `src/core/settings.py` anpassen (`DEBUG` und `DATABASES`)
3. `install.sh` ausführen (erstellt virtual environment, führt Datenbank-Migration aus)
4. `./src/manage.py createsuperuser` ausführen, um Admin-Account zu erstellen
5. Apache2 mit `mod_wsgi` installieren oder `./src/manage.py runserver` ausführen
6. Im Back End unter "administrative divisions" und "zip codes" CSV Import-Funktionen nutzen

# Lizenz
Der Quellcode ist [Apache 2.0](LICENSE.txt) lizenziert. Bootstrap und jQuery stehen unter der MIT Lizenz.
