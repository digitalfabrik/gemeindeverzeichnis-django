# Generated by Django 3.2 on 2021-04-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvz', '0013_administrativedivision_office_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedivision',
            name='division_type',
            field=models.IntegerField(choices=[(10, 'Bundesland'), (20, 'Regierungsbezirk'), (30, 'Region'), (40, 'Kreis'), (41, 'Kreisfreie Stadt (Kreisebene)'), (42, 'Stadtkreis (Kreisebene)'), (43, 'Kreis'), (44, 'Landkreis'), (45, 'Regionalverband'), (50, 'verbandsfreie Gemeinde'), (51, 'Amt'), (52, 'Samtgemeinde'), (53, 'Verbandsgemeinde'), (54, 'Verwaltungsgemeinschaft'), (55, 'Kirchspielslandgemeinde'), (56, 'Verwaltungsverband'), (57, 'VG Trägermodell'), (58, 'Erfüllende Gemeinde'), (60, 'Markt'), (61, 'Kreisfreie Stadt (Gemeindeebene)'), (62, 'Stadtkreis (Gemeindeebene)'), (63, 'Stadt'), (64, 'Kreisangehörige Gemeinde'), (65, 'gemeindefreies Gebiet, bewohnt'), (66, 'gemeindefreies Gebiet, unbewohnt'), (67, 'große Kreisstadt')]),
        ),
    ]
