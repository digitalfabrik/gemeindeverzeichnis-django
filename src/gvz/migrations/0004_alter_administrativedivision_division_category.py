# Generated by Django 3.2 on 2021-04-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvz', '0003_alter_administrativedivision_ags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedivision',
            name='division_category',
            field=models.IntegerField(blank=True),
        ),
    ]
