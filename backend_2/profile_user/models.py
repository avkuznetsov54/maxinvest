from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
# from django.utils.text import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager


def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    password = models.CharField(max_length=128, verbose_name='Пароль')
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='ФИО')
    # active = models.BooleanField(default=False)  # can login

    # timestamp = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    is_active = models.BooleanField(_('active'),
                                    default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ))
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin site.'
                                   ))
    # superuser = models.BooleanField(default=False)  # superuser

    # date_joined = models.DateTimeField(verbose_name=_('Date Joined'),
    #                                    auto_now_add=True, editable=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    update_date = models.DateTimeField(verbose_name=_('date update'),
                                       auto_now=True)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    USERNAME_FIELD = 'email'  # username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = []  # ['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # @property
    # def is_staff(self):
    #     if self.is_superuser:
    #         return True
    #     return self.staff

    # @property
    # def is_superuser(self):
    #     return self.superuser

    # @property
    # def is_active(self):
    #     return self.active
