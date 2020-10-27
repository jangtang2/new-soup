from django.contrib import admin
from . import models


@admin.register(models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Facility)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.ETC)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "city",
        "booklinks",
    )
    list_filter = ("city",)
    search_fields = ("=city", "^name")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass