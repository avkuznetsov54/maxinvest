import os
from django.core.exceptions import ValidationError as DjangoValidationError

from django.db import models

import datetime
from slugify import slugify     # тут используется awesome-slugify
from PIL import Image           # для обработки изображения нам нужен pillow

from project import settings
from geo_location.models import Region, City, District


# !!!!
def generate_url_for_image(self, filename):
    print(self.name)
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    filename = "%s.%s" % (slugify(self.name, to_lower=True), ext)
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


def some_model_thumb_name(instance, filename):
    now = datetime.datetime.now()
    # original_image_path = str(instance.main_image).rsplit('/', 1)[0]
    # return os.path.join(original_image_path, filename)
    url = '/media/images/realestate/%s/%s/%s/%s' % (now.year, now.month, now.day, filename)
    return url


# # ф-ция генерит путь для загружаемого изображения и планировок
# def generate_url_for_image(self, filename):
#     now = datetime.datetime.now()
#     url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
#                                                        now.hour, now.minute, now.second, now.microsecond, filename)
#     return url


# ф-ция генерит путь для загружаемого логотипа застройщика
def generate_url_for_logo_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/logo_image/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class Deadline(models.Model):
    """Модель Срок сдачи"""
    full_date = models.CharField(max_length=10, unique=True, verbose_name='Срок сдачи')
    only_year = models.IntegerField(db_index=True, verbose_name='Год срока сдачи')
    only_quarter = models.IntegerField(db_index=True, verbose_name='Квартал срока сдачи')

    def __str__(self):
        return self.full_date

    class Meta:
        verbose_name = 'Срок сдачи'
        verbose_name_plural = 'Сроки сдачи'
        # ordering = ['name']


class Developer(models.Model):
    """Модель Застройщик"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Застройщик')
    description = models.TextField(blank=True, verbose_name='Описание')
    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип застройщика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'
        ordering = ['name']


class ClassOfHousing(models.Model):
    """Модель Класс Жилья"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Класс Жилья')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс Жилья'
        verbose_name_plural = 'Классы Жилья'
        ordering = ['name']


class FloorInBuilding(models.Model):
    """Модель Этаж"""
    num_floor = models.IntegerField(db_index=True, verbose_name='Этаж')

    def __str__(self):
        return f'{self.num_floor}'

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'
        ordering = ['num_floor']


class NamesOfMetroStations(models.Model):
    """Модель Метро"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    distance_to_center = models.CharField(max_length=50, null=True, blank=True, verbose_name='Расстояние до центра')
    sub_text_distance_to_center = models.CharField(max_length=255, null=True, blank=True,
                                                   verbose_name='Текс для тултипа')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'
        ordering = ['name']


class MaterialWallsOfHouse(models.Model):
    """Модель Материал стен дома"""
    name = models.CharField(max_length=255, unique=True, verbose_name='Материал стен дома')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал стен дома'
        verbose_name_plural = 'Материалы стен дома'
        ordering = ['name']


class ApartmentDecoration(models.Model):
    """Модель Отделка квартиры"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отделка квартиры'
        verbose_name_plural = 'Отделки квартиры'
        ordering = ['name']


class Infrastructure(models.Model):
    """Модель Инфраструктура"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    icon = models.FileField(upload_to=generate_url_for_image,
                            null=True,
                            blank=True,
                            verbose_name="Иконка")
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктура'
        ordering = ['name']


class NumberOfRooms(models.Model):
    """Модель Количество комнат"""
    name = models.CharField(max_length=10, unique=True, verbose_name='Название')
    additional_name = models.CharField(max_length=150, blank=True, verbose_name='Добавочное название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'
        ordering = ['id']


class ResidentialComplex(models.Model):
    """Модель Жилого Комплекса"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')

    is_active_load_data = models.BooleanField(default=False, verbose_name='Включить загруженные данные о квартирах',
                                              help_text='Отключит данные о квартирах, занесенные вручную.')

    name = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Название ЖК')
    url_name = models.CharField(max_length=255, unique=True, verbose_name='URL для этого ЖК',
                                help_text='Для адресной строки в браузере. Только ЛАТИНИИЦА!!! Без: / и пробелов.')

    logo_image = models.FileField(upload_to=generate_url_for_logo_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Логотип ЖК")

    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Застройщик',
                                  related_name="rescomplex_developer",
                                  default=None,
                                  null=True,
                                  blank=True)
    class_of_housing = models.ForeignKey(ClassOfHousing,
                                         on_delete=models.SET_NULL,
                                         verbose_name='Класс Новостройки',
                                         related_name='rescomplex_classofhousing',
                                         default=None,
                                         null=True,
                                         blank=True)
    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='rescomplex_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='rescomplex_city',
                             default=None,
                             null=True,
                             blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='rescomplex_district',
                                 default=None,
                                 null=True,
                                 blank=True)
    address = models.CharField(max_length=150, db_index=True, verbose_name='Адрес',
                               default=None,
                               blank=True)
    one_or_many_buildings = models.BooleanField(default=False, verbose_name='В ЖК несколько строений')

    number_of_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность',
                                            help_text='ОСТАВИТЬ ПУСТЫМ! Если в ЖК несколько строений')

    min_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность min')
    max_storeys = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Этажность max')

    house_completed = models.BooleanField(default=False, verbose_name='Дом сдан, Да/Нет')
    deadline = models.ManyToManyField(Deadline,
                                      verbose_name='Срок сдачи',
                                      related_name='rescomplex_deadline',
                                      default=None,
                                      blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение ЖК")
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    main_image_thumb = models.CharField('Thumbnail image', max_length=255, blank=True)

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(blank=True, verbose_name='Описание')

    distance_to_metro = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Растояние до метро, м')
    metro_stations = models.ManyToManyField(NamesOfMetroStations,
                                            verbose_name='Название ближайщего метро',
                                            related_name='rescomplex_metrostations',
                                            default=None,
                                            blank=True)

    site_developer = models.URLField(max_length=300,
                                     verbose_name='Сайт застройщика/Жилого комплекса',
                                     default=None,
                                     null=True,
                                     blank=True)

    infrastructure = models.ManyToManyField(Infrastructure,
                                            verbose_name='Инфраструктура',
                                            related_name='rescomplex_infrastructure',
                                            default=None,
                                            blank=True)
    material_walls = models.ManyToManyField(MaterialWallsOfHouse,
                                            verbose_name='Материал стен дома',
                                            related_name='rescomplex_materialwalls',
                                            default=None,
                                            blank=True)
    apart_decoration = models.ManyToManyField(ApartmentDecoration,
                                              verbose_name='Отделка',
                                              related_name='rescomplex_apartdecoration',
                                              default=None,
                                              blank=True)
    is_visible_video = models.BooleanField(default=False, verbose_name='Показывать видео')

    # создание миниатюр для "Главное изображение ЖК" будет происходить каждый раз при сохранении модели.
    # Постараемся с этим побороться, добавив в модель следующий метод:
    def __init__(self, *args, **kwargs):
        super(ResidentialComplex, self).__init__(*args, **kwargs)
        self.__original_main_image = self.main_image.url

    def __str__(self):
        return self.name

    # Путь до миниатюры "Главное изображение ЖК"
    def get_thumb_main_image_url(self):
        return settings.MEDIA_URL + self.main_image_thumb

    def save(self, *args, **kwargs):
        if self.main_image.url != self.__original_main_image:

            # size = {'height': 200, 'width': 320}

            super(ResidentialComplex, self).save(*args, **kwargs)
            extension = str(self.main_image.path).rsplit('.', 1)[1]  # получаем расширение загруженного файла
            filename = str(self.main_image.path).rsplit(os.sep, 1)[1].rsplit('.', 1)[0]  # получаем имя загруженного файла (без пути к нему и расширения)
            fullpath = str(self.main_image.path).rsplit(os.sep, 1)[0]  # получаем путь к файлу (без имени и расширения)

            if extension in ['jpg', 'jpeg', 'png']:  # если расширение входит в разрешенный список
                im = Image.open(str(self.main_image.path))  # открываем изображение

                (width, height) = im.size  # получаем width и height загружаемой картинки
                # print('width:', width)
                # print('height:', height)
                new_height = 300  # Высота
                new_width = int(new_height * width / height)
                im.thumbnail((new_width, new_height))

                # im.thumbnail((size['width'], size['height']))  # создаем миниатюру указанной ширины и высоты (важно - im.thumbnail сохраняет пропорции изображения!)
                thumbname = filename + "_" + str(new_width) + "x" + str(
                    new_height) + '.' + extension  # имя нового изображения в формате oldname_60x60.jpg
                im.save(fullpath + os.sep + thumbname, 'JPEG', optimize=True, quality=60)  # сохраняем полученную миниатюру
                self.main_image_thumb = some_model_thumb_name(self, thumbname)  # записываем путь к ней в поле image_thumb в модели
                super(ResidentialComplex, self).save(*args, **kwargs)
        else:
            super(ResidentialComplex, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жилой Комплекс'
        verbose_name_plural = 'Жилые Комплексы'
        ordering = ['name']


class ResidentialPremise(models.Model):
    """Модель Жилого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать, Да/Нет')
    res_complex = models.ForeignKey(ResidentialComplex,
                                    on_delete=models.SET_NULL,
                                    verbose_name='Жилой комплекс',
                                    related_name='respremises_rescomplex',
                                    default=None,
                                    null=True,
                                    blank=True)
    number_rooms = models.ForeignKey(NumberOfRooms,
                                     on_delete=models.SET_NULL,
                                     verbose_name='Количество комнат',
                                     related_name='respremises_numberrooms',
                                     default=None,
                                     null=True)

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена')
    min_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена от, м')
    max_price = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Цена до, м')

    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='respremises_floor',
                                   default=None,
                                   blank=True)

    def __str__(self):
        return f'{self.number_rooms}'

    class Meta:
        verbose_name = 'Жилое помещение'
        verbose_name_plural = 'Жилые помещения'
        # ordering = ['name']


class ImagesResidentialComplex(models.Model):
    """Модель Изображение Жилого Комплекса"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение")
    residential_complex = models.ForeignKey(ResidentialComplex,
                                            verbose_name="Жилой Комплекс",
                                            related_name='images_residential_complex',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Изображение Жилого Комплекса"
        verbose_name_plural = "Изображения Жилого Комплекса"


class FloorPlansResidentialPremise(models.Model):
    """Модель Планировка Жилого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Планировка Жилого помещения")

    residential_premises = models.ForeignKey(ResidentialPremise,
                                             verbose_name="Жилое помещение",
                                             related_name='floor_residential_premises',
                                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Планировка Жилого помещения"
        verbose_name_plural = "Планировки Жилого помещения"


class VideoResidentialComplex(models.Model):
    """Модель Видео Жилого Комплекса"""
    link_on_video = models.URLField(max_length=2000,
                                    verbose_name='Ссылка на видео',
                                    default=None,
                                    null=True,
                                    blank=True)
    residential_complex = models.ForeignKey(ResidentialComplex,
                                            verbose_name="Жилой Комплекс",
                                            related_name='video_residential_complex',
                                            on_delete=models.CASCADE)
    add_text = models.CharField(max_length=300, blank=True, verbose_name='Доплнительный текст')

    class Meta:
        verbose_name = 'Видео Жилого Комплекса'
        verbose_name_plural = 'Видео Жилого Комплекса'
        ordering = ['id']
