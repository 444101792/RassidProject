from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, TicketCommentViewSet

router = DefaultRouter()
router.register("tickets", TicketViewSet)
router.register("comments", TicketCommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
