from django.db import models
from django.contrib.auth.models import User

import datetime

from geo_location.models import Region, City, District, Address
from residential_properties.models import FloorInBuilding, ResidentialComplex


# ф-ция генерит путь для загружаемого изображения и планировок
def generate_url_for_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/realestate/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                       now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class BusinessCategory(models.Model):
    """Модель Категория бизнеса"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория бизнеса'
        verbose_name_plural = 'Категории бизнесов'
        ordering = ['name']


class PurposeOfCommercialPremise(models.Model):
    """Модель Назначение помещения"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Назначение помещения'
        verbose_name_plural = 'Назначении помещений'
        ordering = ['name']


class CookerHood(models.Model):
    """Модель Вытяжка"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вытяжка'
        verbose_name_plural = 'Вытяжки'
        ordering = ['name']


class TypeEntranceToCommercialPremises(models.Model):
    """Модель Тип входа в коммерческое помещение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип входа в коммерческое помещение'
        verbose_name_plural = 'Типы входов в коммерческое помещение'
        ordering = ['name']


class CommunicationSystems(models.Model):
    """Модель Системы коммуникаций"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Системы коммуникаций'
        verbose_name_plural = 'Системы коммуникаций'
        ordering = ['name']


class RelativeLocation(models.Model):
    """Модель Расположение"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
        ordering = ['name']


class CommercialPremises(models.Model):
    """Модель Коммерческого помещения"""
    is_active = models.BooleanField(default=True, verbose_name='Отображать')

    is_group_multiple_objs = models.BooleanField(default=False, verbose_name='Сгруппировать несколько объектов',
                                                 help_text='Если нужно занести несколько помещений в одну карточку.')

    use_contacts_fixed_agent = models.BooleanField(default=False,
                                                   verbose_name='Использовать контакты Закреплённого(-ых) агента(-ов)')
    fixed_agent = models.ManyToManyField(User,
                                         verbose_name='Закреплённый агент',
                                         related_name='compremises_fixedagent',
                                         default=None,
                                         blank=True)

    is_sale = models.BooleanField(default=False, verbose_name='Продажа')
    is_rent = models.BooleanField(default=False, verbose_name='Аренда')

    area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь')
    min_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь от, м')
    max_area = models.FloatField(db_index=True, null=True, blank=True, verbose_name='Площадь до, м')

    floor = models.ManyToManyField(FloorInBuilding,
                                   verbose_name='Этаж',
                                   related_name='compremises_floor',
                                   default=None,
                                   blank=True)

    several_floors = models.BooleanField(default=False, verbose_name='Помещение с несколькими этажами')

    region = models.ForeignKey(Region,
                               on_delete=models.SET_NULL,
                               verbose_name='Область',
                               related_name='compremises_region',
                               default=None,
                               null=True,
                               blank=True)
    city = models.ForeignKey(City,
                             on_delete=models.SET_NULL,
                             verbose_name='Город',
                             related_name='compremises_city',
                             default=None,
                             null=True,
                             blank=True)
    district = models.ForeignKey(District,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Район',
                                 related_name='compremises_district',
                                 default=None,
                                 null=True,
                                 blank=True)
    # address = models.CharField(max_length=150, default=None, blank=True, verbose_name='Адрес')
    address = models.ForeignKey(Address,
                                on_delete=models.SET_NULL,
                                verbose_name='Адрес',
                                related_name='compremises_address',
                                default=None,
                                null=True,
                                blank=False)

    relative_location = models.ManyToManyField(RelativeLocation,
                                               verbose_name='Расположение',
                                               related_name='compremises_relativelocation',
                                               default=None,
                                               blank=True)

    residential_complex = models.ForeignKey(ResidentialComplex,
                                            on_delete=models.SET_NULL,
                                            verbose_name='Жилой комплекс',
                                            related_name='compremises_rescomplex',
                                            default=None,
                                            null=True,
                                            blank=True)

    building_commercial_premise = models.BooleanField(default=False, verbose_name='Строящее',
                                                      help_text='Находиться в процессе строительства.')

    finished_commercial_premise = models.BooleanField(default=False, verbose_name='Готовое',
                                                      help_text='Построенное помещение.')

    purpose_commercial_premise = models.ManyToManyField(PurposeOfCommercialPremise,
                                                        verbose_name='Назначение коммерческого помещения',
                                                        related_name='compremises_purpose',
                                                        default=None,
                                                        blank=True)
    business_category = models.ManyToManyField(BusinessCategory,
                                               verbose_name='Категория бизнеса',
                                               related_name='compremises_businesscategory',
                                               default=None,
                                               blank=True)

    rent_price_sq_m = models.IntegerField(db_index=True, null=True, blank=True,
                                          verbose_name='Стоимость аренды, руб/кв.м.')
    rent_price_month = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоимость аренды, руб/мес.')

    cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                       verbose_name='Стоймость на продажу')
    min_cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоймость на продажу, от')
    max_cost_of_sale = models.IntegerField(db_index=True, null=True, blank=True,
                                           verbose_name='Стоймость на продажу, до')

    min_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость от, мес')
    max_payback = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='Окупаемость до, мес')
    min_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка от, руб/кв.м.')
    max_average_rental_rate = models.IntegerField(db_index=True, null=True, blank=True,
                                                  verbose_name='Средняя арендная ставка до, руб/кв.м.')
    possible_income = models.IntegerField(db_index=True, null=True, blank=True,
                                          verbose_name='Возможный доход, руб/мес.')

    kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт')
    min_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, от')
    max_kw = models.FloatField(db_index=True, null=True, blank=True, verbose_name='кВт, до')
    comment_kw = models.CharField(max_length=255, blank=True,
                                  verbose_name='Комментарий к "кВт"')

    communication_systems = models.ManyToManyField(CommunicationSystems,
                                                   verbose_name='Системы коммуникаций',
                                                   related_name='compremises_comsystems',
                                                   default=None,
                                                   blank=True)
    cooker_hood = models.ManyToManyField(CookerHood,
                                         verbose_name='Вытяжка',
                                         related_name='compremises_cookerhood',
                                         default=None,
                                         blank=True)
    type_entrance = models.ManyToManyField(TypeEntranceToCommercialPremises,
                                           verbose_name='Тип входа',
                                           related_name='compremises_typeentrance',
                                           default=None,
                                           blank=True)
    main_image = models.FileField(upload_to=generate_url_for_image,
                                  null=True,
                                  blank=True,
                                  verbose_name="Главное изображение помещения")
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")

    longitude = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    latitude = models.FloatField(null=True, blank=True, verbose_name='Широта')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Коммерческое помещение'
        verbose_name_plural = 'Коммерческие помещения'
        # ordering = ['name']


class ImagesCommercialPremises(models.Model):
    """Модель Изображение Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Изображение")
    commercial_premises = models.ForeignKey(CommercialPremises,
                                            verbose_name="Коммерческое помещение",
                                            related_name='images_commercial_premises',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Изображение Коммерческого помещения"
        verbose_name_plural = "Изображения Коммерческого помещения"


class FloorPlansCommercialPremises(models.Model):
    """Модель Планировка Коммерческого помещения"""
    alt_attr = models.CharField(max_length=300, blank=True, verbose_name="img alt")
    image = models.FileField(upload_to=generate_url_for_image,
                             null=True,
                             blank=True,
                             verbose_name="Планировка Коммерческого помещения")
    commercial_premises = models.ForeignKey(CommercialPremises,
                                            verbose_name="Коммерческое помещение",
                                            related_name='floorplans_commercial_premises',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Планировка Коммерческого помещения"
        verbose_name_plural = "Планировки Коммерческого помещения"


class VideoCommercialPremises(models.Model):
    """Модель Видео Коммерческого помещения"""
    link_on_video = models.URLField(max_length=2000,
                                    verbose_name='Ссылка на видео',
                                    default=None,
                                    null=True,
                                    blank=True)
    commercial_premises = models.ForeignKey(CommercialPremises,
                                            verbose_name="Коммерческое помещение",
                                            related_name='video_commercial_premises',
                                            on_delete=models.CASCADE)
    add_text = models.CharField(max_length=300, blank=True, verbose_name='Доплнительный текст')

    class Meta:
        verbose_name = 'Видео Коммерческого помещения'
        verbose_name_plural = 'Видео Коммерческого помещения'
        ordering = ['id']
