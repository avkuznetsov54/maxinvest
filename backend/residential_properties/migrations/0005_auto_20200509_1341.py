# Generated by Django 3.0.6 on 2020-05-09 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('residential_properties', '0004_auto_20200509_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoresidentialcomplex',
            name='residential_complex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_residential_complex', to='residential_properties.ResidentialComplex', verbose_name='Жилой Комплекс'),
        ),
    ]