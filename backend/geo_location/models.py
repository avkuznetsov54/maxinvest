from django.db import models

import datetime


def generate_url_for_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/geo/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class Region(models.Model):
    """Модель Область"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")

    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'
        ordering = ['name']


class City(models.Model):
    """Модель Город"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='city_region',
                               default=None,
                               null=True,
                               blank=False)

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class District(models.Model):
    """Модель Района"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Район')
    subname = models.CharField(max_length=10, unique=True, blank=True, verbose_name='Сокращённое название')
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='district_city',
                             default=None,
                             null=True,
                             blank=False)

    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Изображение")
    alt_attr = models.CharField(max_length=300, null=True, blank=True, verbose_name="img alt")
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['name']
