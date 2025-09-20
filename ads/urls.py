from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .apps import AdsConfig
from .views import AdsViewsSet, ReviewViewSet

app_name = AdsConfig.name

router = routers.DefaultRouter()
router.register(r"", AdsViewsSet, basename="ads")
ads_router = routers.NestedDefaultRouter(router, r"", lookup="ad")
ads_router.register(r"reviews", ReviewViewSet, basename="ad-reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(ads_router.urls))
]
