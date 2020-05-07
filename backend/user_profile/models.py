from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime


# ф-ция генерит путь для загружаемого фото user
def generate_url_for_user_image(self, filename):
    now = datetime.datetime.now()
    url = 'images/users/%s/%s/%s/%s%s%s-%s-%s' % (now.year, now.month, now.day,
                                                  now.hour, now.minute, now.second, now.microsecond, filename)
    return url


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')

    is_commercia = models.BooleanField(default=False, verbose_name='Коммерческая')
    is_residential = models.BooleanField(default=False, verbose_name='Жилая')

    full_name = models.CharField(max_length=255, db_index=True, blank=True, verbose_name='ФИО')

    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон',
                                    help_text='Без пробелов, скобок, +7 и 8. <p style="color:red;font-size:18px;">ТОЛЬКО ЦИФРЫ !!!</p>')

    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    image = models.FileField(upload_to=generate_url_for_user_image,
                             null=True,
                             blank=True,
                             verbose_name="Фото")

    bio = models.TextField(blank=True, verbose_name='О себе')

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.profile.save()

# TODO: дествия с useer model
# @receiver(post_save, sender=User)
# def create_user_post(sender, instance, created, **kwargs):
#     """Отправка email о смене пароля пользователя"""
#     if created:
#         send_mail_edit_password(instance)
