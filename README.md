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
* `id`: Datenbank-ID
* `ags`: offizieller Gemeindeschlüssel
* `name`: Name der Gemeinde, Kreis, Land, etc
* `division_category`: Kategorie-ID (Bundesland, Regierungsbezirk, Region, Kreis, Gemeindeverband, Gemeinde)
* `division_category_name`: Kategorie-Name
* `division_type`: Offizieller Kennziffer/Bezeichner für die administrative Einheit (Markt, Samtgemeinde, etc)
* `division_type_name`: Bezeichnung des Typs der administrativen Einheit
* `office_zip`: Postleitzahl der Anschrift
* `office_street`: Straße der Anschrift
* `office_city`: Stadt der Anschrift
* `area`: Fläche in km²
* `citizens_total`: Einwohner:innen
* `citizens_male`: männliche Einwohner
* `citizens_female`: weibliche Einwohnerinnen
* `population_density`: Bevölkerungsdichte pro Quadratkilometer
* `longitude`: Längengrad
* `latitude`: Breitengrad
* `travel_name`: Reisegebietsname
* `travel_code`: Reisegebietskennziffer
* `url`: Pfad zum Object
* `parent`: Pfad zum übergeordneten Projekt
* `children`: Liste der Pfade zu untergeordneten Objekten
* `zip_codes`: Liste aller untergeordneter Postleitzahlen

Folgende Kategorien können zum Filtern genutzt werden:
* Gemeindeschlüssel
* Administrative Kategorie (Bundesland (`10`), Regierungsbezirk (`20`), Region (`30`), Kreis (`40`), Gemeindeverband (`50`), Gemeinde (`60`))
* Name
* Übergeordnete administrative Einheit ID

# Lizenz
Der Quellcode ist [Apache 2.0](LICENSE.txt) lizenziert.
