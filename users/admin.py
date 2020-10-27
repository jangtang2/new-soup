from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    list_display = ("username", "email", "date_joined", "admin")
    list_filter = ("date_joined", "admin")