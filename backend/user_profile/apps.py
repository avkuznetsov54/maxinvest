from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile'
    verbose_name = 'Данные для профиля пользователя'

    def ready(self):
        import user_profile.signals
