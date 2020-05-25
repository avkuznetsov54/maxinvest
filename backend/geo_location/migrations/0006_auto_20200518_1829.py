# Generated by Django 3.0.6 on 2020-05-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0005_auto_20200518_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['name'], 'verbose_name': 'Адрес (Улица и Номер дома)', 'verbose_name_plural': 'Адреса (Улицы и Номера домов)'},
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
    ]