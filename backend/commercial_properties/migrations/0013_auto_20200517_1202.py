# Generated by Django 3.0.6 on 2020-05-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial_properties', '0012_auto_20200517_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialpremises',
            name='is_group_multiple_objs',
            field=models.BooleanField(default=False, help_text='Если нужно занести несколько помещений в одну карточку.', verbose_name='Сгруппировать несколько объектов'),
        ),
        migrations.AlterField(
            model_name='commercialpremises',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Отображать'),
        ),
    ]
