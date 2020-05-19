# Generated by Django 3.0.6 on 2020-05-19 17:24

from django.db import migrations, models
import residential_properties.models


class Migration(migrations.Migration):

    dependencies = [
        ('residential_properties', '0011_auto_20200518_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorplansresidentialpremise',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_floor_plan, verbose_name='Планировка Жилого помещения'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='main_image_thumb',
            field=models.FileField(blank=True, null=True, upload_to=residential_properties.models.generate_url_for_image, verbose_name='Thumbnail image'),
        ),
    ]
