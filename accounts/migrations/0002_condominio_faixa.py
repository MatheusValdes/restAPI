# Generated by Django 3.1.2 on 2021-07-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarifas', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='faixa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tarifas.faixas'),
        ),
    ]
