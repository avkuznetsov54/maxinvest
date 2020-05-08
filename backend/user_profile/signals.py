from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


# TODO: эта хреновина ведёт себя странно !!!
# если раскоментировать то будет ошибка при заполнении полей класса Profile при создании юзера из админки.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    print(created)  # allways True

    if created:

        Profile.objects.create(user=instance)


        # users_without_profile = User.objects.filter(profile__isnull=True)
        # for user in users_without_profile:
        #     Profile.objects.create(user=user)

    instance.profile.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
