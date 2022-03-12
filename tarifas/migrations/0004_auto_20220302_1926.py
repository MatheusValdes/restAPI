# Generated by Django 3.1.2 on 2022-03-02 22:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0003_auto_20210716_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_tarifa',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='tarifa', unique_with=('empresa__nome',)),
        ),
    ]
