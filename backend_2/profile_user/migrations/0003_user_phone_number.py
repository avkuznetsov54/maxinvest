# Generated by Django 3.0.6 on 2020-05-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0002_auto_20200524_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Без пробелов, скобок, +7 и 8. <b style="color:red;font-size:10px;">ТОЛЬКО ЦИФРЫ !!!</b><br>Пример: 9131112233', max_length=20, verbose_name='Телефон'),
        ),
    ]
