from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#
#     # print(dir(User))
#     print(User.profile)
#
#     # TODO: [РЕШЕНО] магическое строчка кода !!!
#     #  которая решает проблему "User has no profile" при создании юзера с related model Profile,
#     #  с помощью OneToOneField
#     # User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
#     # User.profile = property(lambda u: Profile.objects.update_or_create(user=u)[0])
#
#     # if created:
#     # Profile.objects.create(user=instance)
#
#     # instance.profile.save()


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         # Profile.objects.create(user=instance)
#
#         profile, new = Profile.objects.get_or_created(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # print('1 ===================')
    # print(instance)
    # print(sender.objects.all())
    # print('2 ===================')
    # print(sender.objects.get(username=instance).email)
    # # print(sender.objects.get(username=instance).profile)
    # print('3 ===================')

    try:

        # print(instance.profile)
        instance.profile.save()

    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        Profile.objects.create(user=instance)

    # Profile.objects.create(user=instance) # если передоваемых данных в профиле нет - раскоментировать!
    # instance.profile.save()

    # print('4 ===================')

