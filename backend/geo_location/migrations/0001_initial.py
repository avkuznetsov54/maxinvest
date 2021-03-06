# Generated by Django 3.0.6 on 2020-05-07 17:03

from django.db import migrations, models
import django.db.models.deletion
import geo_location.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('main_image', models.FileField(blank=True, null=True, upload_to=geo_location.models.generate_url_for_image, verbose_name='Изображение')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('main_image', models.FileField(blank=True, null=True, upload_to=geo_location.models.generate_url_for_image, verbose_name='Изображение')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Район')),
                ('subname', models.CharField(blank=True, max_length=10, unique=True, verbose_name='Сокращённое название')),
                ('main_image', models.FileField(blank=True, null=True, upload_to=geo_location.models.generate_url_for_image, verbose_name='Изображение')),
                ('alt_attr', models.CharField(blank=True, max_length=300, null=True, verbose_name='img alt')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_city', to='geo_location.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city_region', to='geo_location.Region', verbose_name='Область'),
        ),
    ]
