from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirportViewSet, AirportUserViewSet, AirportSubscriptionViewSet

router = DefaultRouter()
router.register("airports", AirportViewSet)
router.register("users", AirportUserViewSet)
router.register("subscriptions", AirportSubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
