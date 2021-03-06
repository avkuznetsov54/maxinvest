# Generated by Django 3.0.6 on 2020-05-18 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_location', '0004_auto_20200518_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='street',
            options={'ordering': ['name'], 'verbose_name': 'Улица', 'verbose_name_plural': 'Улицы'},
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Адрес')),
                ('numhouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_numhouse', to='geo_location.NumHouse', verbose_name='Номер дома / корпуса')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_street', to='geo_location.Street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Улица и Номер дома',
                'verbose_name_plural': 'Улицы и Номера домов',
                'ordering': ['name'],
            },
        ),
    ]
