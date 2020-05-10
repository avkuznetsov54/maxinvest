# Generated by Django 3.0.6 on 2020-05-09 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercial_properties', '0005_auto_20200508_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorplanscommercialpremises',
            name='commercial_premises',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floorplans_commercial_premises', to='commercial_properties.CommercialPremises', verbose_name='Коммерческое помещение'),
        ),
        migrations.AlterField(
            model_name='imagescommercialpremises',
            name='commercial_premises',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_commercial_premises', to='commercial_properties.CommercialPremises', verbose_name='Коммерческое помещение'),
        ),
    ]