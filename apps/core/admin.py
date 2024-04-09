from django.contrib import admin

from .models import AppUser, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_filter = ["continent", "economy"]


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass
