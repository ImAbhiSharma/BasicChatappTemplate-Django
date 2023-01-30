from django.contrib import admin
from .models import AppUser


class AppUserAdmin (admin.ModelAdmin):
    list_display = ("firstname", "lastname", "last_seen")

admin.site.register (AppUser, AppUserAdmin)