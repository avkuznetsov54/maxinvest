from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Region, City, District


class CityInline(admin.TabularInline):
    model = City
    extra = 1


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)
    inlines = (CityInline, )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'description')
    list_display_links = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subname', 'city')
    list_display_links = ('name',)
