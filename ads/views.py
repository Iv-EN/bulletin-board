from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.permissions import AdsPermissions, ReviewPermissions

from .models import Advertisement, Review
from .paginators import AdsPaginator
from .serializer import AdvertisementSerializer, ReviewSerializer


class AdsViewsSet(ModelViewSet):
    """Viewset для объявлений."""

    queryset = (
        Advertisement.objects.all()
        .select_related("author")
        .prefetch_related("reviews")
    )
    serializer_class = AdvertisementSerializer
    permission_classes = [AdsPermissions]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["title"]
    pagination_class = AdsPaginator
    ordering_fields = ["-created_at", "price"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        action = getattr(self, "action", None)
        if action in ("list", "retrieve"):
            return [AllowAny()]
        return [AdsPermissions()]


class ReviewViewSet(ModelViewSet):
    """Viewset для комментариев к объявлениям."""

    queryset = Review.objects.all().select_related("author", "ad")
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermissions]
    filter_backends = []

    def get_queryset(self):
        qs = super().get_queryset()
        ad_pk = self.kwargs.get("ad_pk")
        if ad_pk:
            qs = qs.filter(ad_id=ad_pk)
        return qs

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Advertisement, pk=ad_pk)
        serializer.save(ad=ad, author=self.request.user)
