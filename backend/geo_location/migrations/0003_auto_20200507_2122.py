# Generated by Django 3.0.6 on 2020-05-07 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0002_district_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_city', to='geo_location.City', verbose_name='Город'),
        ),
    ]
