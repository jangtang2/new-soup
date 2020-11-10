from django.contrib import admin
from . import models


@admin.register(models.Fav)
class FavAdmin(admin.ModelAdmin):

    list_display = ("name", "user", "count_places")

    filter_horizontal = ("places",)