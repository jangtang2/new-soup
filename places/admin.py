from django.contrib import admin
from django.utils.html import mark_safe
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


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

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
        "total_rating",
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

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_discription = "Thumbnail"