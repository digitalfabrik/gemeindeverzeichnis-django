# Generated by Django 3.2 on 2021-04-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvz', '0002_auto_20210424_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedivision',
            name='ags',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
