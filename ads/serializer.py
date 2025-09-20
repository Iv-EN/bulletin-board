from rest_framework import serializers

from .models import Advertisement, Review


class AdvertisementSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "price",
            "description",
            "author",
            "created_at",
        )
        read_only_field = ("created_at",)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="email")
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")

    class Meta:
        model = Review
        fields = (
            "id",
            "text",
            "author",
            "ad",
            "created_at",
        )
        read_only_fields = ("author", "ad", "created_at")
