# Generated by Django 3.0.6 on 2020-05-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Женский'), ('male', 'Мужской')], max_length=25, verbose_name='Пол'),
        ),
    ]