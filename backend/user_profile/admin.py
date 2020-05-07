from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
    # fields = ('is_residential',) # оставляет для отображения в админке


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
                    'username',
                    'get_full_name',
                    'get_phone_number',
                    'email',
                    'get_is_commercia',
                    'get_is_residential',
                    # 'last_name',
                    'is_staff',
                    # 'is_superuser',
                    'is_active',
    )
    # TODO: решить как использовать поля модели UserProfile в list_filter и search_fields модели User
    # list_filter = ('is_active',)
    list_filter = ['is_active']
    # search_fields = ('get_full_name',)
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
    inlines = (UserProfileInline,)
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
        return obj.userprofile.full_name

    get_full_name.short_description = 'ФИО'
    get_full_name.admin_order_field = 'userprofile__full_name'

    def get_phone_number(self, obj):
        return obj.userprofile.phone_number

    get_phone_number.short_description = 'Телефон'
    get_phone_number.admin_order_field = 'userprofile__phone_number'

    def get_is_commercia(self, obj):
        return obj.userprofile.is_commercia

    get_is_commercia.short_description = 'Коммерция'
    get_is_commercia.admin_order_field = 'userprofile__is_commercia'
    get_is_commercia.boolean = True

    def get_is_residential(self, obj):
        return obj.userprofile.is_residential

    get_is_residential.short_description = 'Жилая'
    get_is_residential.admin_order_field = 'userprofile__is_residential'
    get_is_residential.boolean = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
