from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Profile


class CommercialFilter(admin.SimpleListFilter):
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
    title = 'Коммерция'
    parameter_name = 'is_commercial'

    def lookups(self, request, model_admin):

        return (
            ('True', _('Да')),
            ('False', _('Нет')),
        )

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(profile__is_commercial=self.value())
        else:
            return queryset


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
    # fields = ('is_residential',) # оставляет для отображения в админке
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (
                ('is_commercial', 'is_residential'),
            ),
        }),
        (None, {
            'fields': (
                'full_name',
                'phone_number',
                'birth_date',
            ),
        }),
        (None, {
            'fields': (
                'image', 'get_image',
                'bio',
            ),
        }),
    )


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        'username',
        'get_full_name',
        'get_phone_number',
        'email',
        'get_is_commercial',
        'get_is_residential',
        # 'last_name',
        'is_staff',
        # 'is_superuser',
        'is_active',
    )

    # TODO: [РЕШЕНО] решить как использовать поля модели Profile в list_filter и search_fields модели User
    # https://tproger.ru/translations/extending-django-user-model/#var2
    list_filter = ('is_active', CommercialFilter,)

    search_fields = ('username', 'email', 'profile__full_name', 'profile__phone_number', )
    # Стандартные поля в модели User
    # date_joined, email, first_name, groups, id,
    # is_active, is_staff, is_superuser, last_login, last_name,
    # logentry, password, profile, user_permissions, username

    # fieldsets = (
    #     (None, {'fields': ('username', 'password', 'email')}),
    #     # (('Personal info'), {
    #     #     'fields': ('first_name', 'last_name', 'email')
    #     # }),
    #     (('Permissions'), {
    #         'classes': ('collapse',),
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
    #     }),
    #     (('Important dates'), {
    #         'classes': ('collapse',),
    #         'fields': ('last_login', 'date_joined')
    #     }),
    # )

    list_editable = ['is_active']
    inlines = (ProfileInline,)
    save_on_top = True
    save_as = True

    class Meta:
        model = User

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Если у пользователя есть доступ в админку запрещаем для него отображение суперпользователя
        return qs.filter(is_superuser=False)

    def get_readonly_fields(self, request, obj=None):
        # Запрещённые поля для редактирования для пользователя с доступом в админку
        return () if request.user.is_superuser else ('is_staff', 'is_superuser', 'groups', 'user_permissions')

    def get_full_name(self, obj):
        return obj.profile.full_name

    get_full_name.short_description = 'ФИО'
    get_full_name.admin_order_field = 'profile__full_name'

    def get_phone_number(self, obj):
        return obj.profile.phone_number

    get_phone_number.short_description = 'Телефон'
    get_phone_number.admin_order_field = 'profile__phone_number'

    def get_is_commercial(self, obj):
        return obj.profile.is_commercial

    get_is_commercial.short_description = 'Коммерция'
    get_is_commercial.admin_order_field = 'profile__is_commercial'
    get_is_commercial.boolean = True

    def get_is_residential(self, obj):
        return obj.profile.is_residential

    get_is_residential.short_description = 'Жилая'
    get_is_residential.admin_order_field = 'profile__is_residential'
    get_is_residential.boolean = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
