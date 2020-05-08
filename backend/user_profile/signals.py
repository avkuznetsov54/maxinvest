from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    # TODO: магическое строчка кода,
    #  которая решает проблему "User has no profile" при создании юзера с related model Profile,
    #  с помощью OneToOneField
    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

    instance.profile.save()

