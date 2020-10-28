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

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": ("name", "description", "city", "address"),
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "toilets",
                    "showerbooths",
                )
            },
        ),
        (
            "More About The Space",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "etcs",
                )
            },
        ),
        (
            "For Reservation",
            {"fields": ("booklinks",)},
        ),
    )

    list_display = (
        "name",
        "city",
        "booklinks",
    )

    list_filter = ("city",)
    search_fields = ("=city", "^name")
    filter_horizontal = (
        "amenities",
        "facilities",
        "etcs",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass