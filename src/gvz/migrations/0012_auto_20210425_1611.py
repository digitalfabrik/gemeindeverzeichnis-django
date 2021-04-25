# Generated by Django 3.2 on 2021-04-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvz', '0011_auto_20210425_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedivision',
            name='division_category',
            field=models.IntegerField(choices=[(10, 'Bundesland'), (20, 'Regierungsbezirk'), (30, 'Region'), (40, 'Kreis'), (50, 'Gemeindeverband'), (60, 'Gemeinde')]),
        ),
        migrations.AlterField(
            model_name='administrativedivision',
            name='division_type',
            field=models.IntegerField(choices=[(10, 'Bundesland'), (20, 'Regierungsbezirk'), (30, 'Region'), (40, 'Kreis'), (41, 'Kreisfreie Stadt'), (42, 'Stadtkreis'), (43, 'Kreis'), (44, 'Landkreis'), (45, 'Regionalverband'), (50, 'verbandsfreie Gemeinde'), (51, 'Amt'), (52, 'Samtgemeinde'), (53, 'Verbandsgemeinde'), (54, 'Verwaltungsgemeinschaft'), (55, 'Kirchspielslandgemeinde'), (56, 'Verwaltungsverband'), (57, 'VG Trägermodell'), (58, 'Erfüllende Gemeinde'), (60, 'Markt'), (61, 'Kreisfreie Stadt'), (62, 'Stadtkreis'), (63, 'Stadt'), (64, 'Kreisangehörige Gemeinde'), (65, 'gemeindefreies Gebiet, bewohnt'), (66, 'gemeindefreies Gebiet, unbewohnt'), (67, 'große Kreisstadt')]),
        ),
    ]