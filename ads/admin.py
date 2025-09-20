from django.contrib import admin

from .models import Advertisement, Review


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "title",
        "price",
        "description",
        "author",
        "created_at",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ("id", "text", "ad", "author", "created_at")
