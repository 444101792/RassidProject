from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Airport, AirportUser, AirportSubscription
from .serializers import AirportSerializer, AirportUserSerializer, AirportSubscriptionSerializer
from users.permissions import IsSuperAdmin, IsAirportAdmin

class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

class AirportUserViewSet(ModelViewSet):
    queryset = AirportUser.objects.all()
    serializer_class = AirportUserSerializer
    permission_classes = [IsAuthenticated, IsAirportAdmin]

class AirportSubscriptionViewSet(ModelViewSet):
    queryset = AirportSubscription.objects.all()
    serializer_class = AirportSubscriptionSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
