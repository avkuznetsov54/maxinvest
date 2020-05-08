from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import Textarea, TextInput

from .models import Region, City, District


class CityInline(admin.TabularInline):
    model = City
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 50})},
    }


class DistrictInline(admin.TabularInline):
    model = District
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 50})},
    }


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)
    inlines = (CityInline, )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'description')
    list_display_links = ('name',)
    inlines = (DistrictInline,)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subname', 'city')
    list_display_links = ('name',)
