from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

# ф-ция генерит путь для загружаемого фото user
from django.utils.safestring import mark_safe


def generate_url_for_user_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/users/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                  now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class Specialization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='profile')

    is_commercial = models.BooleanField(default=False, verbose_name='Коммерческая')
    is_residential = models.BooleanField(default=False, verbose_name='Жилая')

    specialization = models.ManyToManyField(Specialization,
                                            verbose_name='Специализация',
                                            related_name='profile_specialization',
                                            default=None,
                                            blank=True)

    full_name = models.CharField(max_length=255, db_index=True, blank=True, verbose_name='ФИО')

    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон',
                                    help_text='Без пробелов, скобок, +7 и 8. '
                                              '<b style="color:red;font-size:10px;">ТОЛЬКО ЦИФРЫ !!!</b><br>'
                                              'Пример: 9131112233')

    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения')

    image = models.FileField(upload_to=generate_url_for_user_image,
                             null=True,
                             blank=True,
                             verbose_name="Фото")

    bio = models.TextField(blank=True, verbose_name='О себе')

    def __str__(self):
        return f'{self.user}'

    def get_image(self):
        return mark_safe(f'<img src={self.image.url} height="150"')

    get_image.short_description = "Изображение"
    get_image.allow_tags = True


# если раскоментировать то будет ошибка при заполнении полей класса Profile при создании юзера из админки.
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         # instance.profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# TODO: дествия с useer model
# @receiver(post_save, sender=User)
# def create_user_post(sender, instance, created, **kwargs):
#     """Отправка email о смене пароля пользователя"""
#     if created:
#         send_mail_edit_password(instance)
