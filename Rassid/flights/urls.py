from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, GateAssignmentViewSet, FlightStatusHistoryViewSet

router = DefaultRouter()
router.register("flights", FlightViewSet)
router.register("gate-assignments", GateAssignmentViewSet)
router.register("status-history", FlightStatusHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
