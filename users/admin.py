from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email", "first_name", "last_name")
