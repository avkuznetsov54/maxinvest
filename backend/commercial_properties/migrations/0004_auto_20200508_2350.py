# Generated by Django 3.0.6 on 2020-05-08 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercial_properties', '0003_auto_20200508_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocommercialpremises',
            name='commercial_premises',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_compremises', to='commercial_properties.CommercialPremises', verbose_name='Коммерческое помещение'),
        ),
    ]