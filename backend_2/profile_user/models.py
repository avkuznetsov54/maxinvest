from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
# from django.utils.text import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.safestring import mark_safe

import datetime

from .managers import UserManager


def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])


class Specialization(models.Model):
    """Модель Специализация"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=10, unique=True, default=None, verbose_name='Короткое название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['name']


class User(AbstractBaseUser, PermissionsMixin):
    """Модель Профиль юзера"""

    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    password = models.CharField(max_length=128, verbose_name='Пароль')
    full_name = models.CharField(max_length=255, null=True,  blank=True, verbose_name='ФИО')

    specialization = models.ManyToManyField(Specialization,
                                            verbose_name='Специализация',
                                            related_name='profile_specialization',
                                            default=None,
                                            blank=True)
    GENDER_CHOICES = (
        ('female', 'Женский'),
        ('male', 'Мужской'),
    )
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=25,
                              blank=True,
                              verbose_name='Пол')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения',
                                  help_text='Формат: YYYY-MM-DD')
    bio = models.TextField(blank=True, verbose_name='О себе')

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


class SocialNetwork(models.Model):
    """Модель Социальная сеть"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    SOCNET_CHOICES = (
        ('whatsapp', 'Whatsapp'),
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('vk', 'VK'),
        ('twitter', 'Twitter'),
    )
    name = models.CharField(choices=SOCNET_CHOICES, max_length=25, blank=True,
                            verbose_name='Социальная сеть')
    link_on_socnet = models.URLField(max_length=2000,
                                     verbose_name='Ссылка',
                                     default=None,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
        ordering = ['name']
