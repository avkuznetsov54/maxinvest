# Generated by Django 3.0.6 on 2020-05-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0006_auto_20200518_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес'),
        ),
    ]
