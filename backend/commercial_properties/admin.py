from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (BusinessCategory, PurposeOfCommercialPremise, CookerHood, TypeEntranceToCommercialPremises,
                     CommunicationSystems, RelativeLocation, CommercialPremises,
                     ImagesCommercialPremises, FloorPlansCommercialPremises, VideoCommercialPremises)


class ImagesCommercialPremisesInline(admin.TabularInline):
    model = ImagesCommercialPremises
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


class FloorPlansCommercialPremisesInline(admin.TabularInline):
    model = FloorPlansCommercialPremises
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="70"')

    get_image.short_description = "Изображение"


class VideoCommercialPremisesInline(admin.TabularInline):
    model = VideoCommercialPremises
    extra = 1


@admin.register(ImagesCommercialPremises)
class ImagesCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(FloorPlansCommercialPremises)
class FloorPlansCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_attr')
    list_display_links = ('id',)


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(PurposeOfCommercialPremise)
class PurposeOfCommercialPremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CookerHood)
class CookerHoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(TypeEntranceToCommercialPremises)
class TypeEntranceToCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CommunicationSystems)
class CommunicationSystemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(RelativeLocation)
class RelativeLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)


@admin.register(CommercialPremises)
class CommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'district', 'area', 'is_sale', 'is_rent', 'is_active')
    list_display_links = ('address',)
    list_filter = ('is_active', 'is_sale', 'is_rent', 'district',)
    search_fields = ("address",)
    inlines = [ImagesCommercialPremisesInline, FloorPlansCommercialPremisesInline, VideoCommercialPremisesInline]
    save_on_top = True
    save_as = True
    list_editable = ("is_active",)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            'fields': (
                'is_active',
                'is_group_multiple_objs',
                ('is_sale', 'is_rent'),
            ),
        }),
        (None, {
            'fields': ('use_contacts_fixed_agent',
                       'fixed_agent',
                       # 'get_fixed_agent',
                       ),
        }),
        (None, {
            'fields': ('area',
                       'min_area',
                       'max_area',
                       'several_floors',
                       'floor',
                       'region',
                       'city',
                       'district',
                       'address',
                       'relative_location',
                       'residential_complex',
                       'building_commercial_premise',
                       'finished_commercial_premise',
                       'purpose_commercial_premise',
                       'business_category',
                       ),
        }),
        (None, {
            'fields': (
                ('rent_price_sq_m', 'rent_price_month'),
                'cost_of_sale',
                ('min_cost_of_sale', 'max_cost_of_sale'),
                ('min_payback', 'max_payback'),
                ('min_average_rental_rate', 'max_average_rental_rate'),
                'possible_income',
            ),
        }),
        (None, {
            'fields': ('kw',
                       'min_kw',
                       'max_kw',
                       'comment_kw',
                       'communication_systems',
                       'cooker_hood',
                       'type_entrance',
                       ),
        }),
        (None, {
            'fields': ('description',
                       ),
        }),
        (None, {
            'fields': ('longitude',
                       'latitude',
                       ),
        }),
        (None, {
            'fields': ('alt_attr',
                       ('main_image', 'get_image'),
                       ),
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} height="70"')

    get_image.short_description = ''

    # def get_fixed_agent(self, obj):
    #     return obj


@admin.register(VideoCommercialPremises)
class VideoCommercialPremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_on_video', 'add_text')
    list_display_links = ('id',)


admin.site.site_title = "BROKERNSK.PRO"
admin.site.site_header = "BROKERNSK.PRO"
