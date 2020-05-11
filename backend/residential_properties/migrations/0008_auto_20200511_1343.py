# Generated by Django 3.0.6 on 2020-05-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residential_properties', '0007_residentialcomplex_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentdecoration',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classofhousing',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developer',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='floorplansresidentialpremise',
            name='alt_attr',
            field=models.CharField(blank=True, default='text', max_length=300, verbose_name='img alt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagesresidentialcomplex',
            name='alt_attr',
            field=models.CharField(blank=True, default='text', max_length=300, verbose_name='img alt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='materialwallsofhouse',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='namesofmetrostations',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='numberofrooms',
            name='additional_name',
            field=models.CharField(blank=True, default='text', max_length=150, verbose_name='Добавочное название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='numberofrooms',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='address',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='alt_attr',
            field=models.CharField(blank=True, default='text', max_length=300, verbose_name='img alt'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='description',
            field=models.TextField(blank=True, default='text', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residentialcomplex',
            name='url_name',
            field=models.CharField(default='text', help_text='Для адресной строки в браузере. Только ЛАТИНИИЦА!!! Без: / и пробелов.', max_length=255, unique=True, verbose_name='URL для этого ЖК'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videoresidentialcomplex',
            name='add_text',
            field=models.CharField(blank=True, default='text', max_length=300, verbose_name='Доплнительный текст'),
            preserve_default=False,
        ),
    ]