from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Flight, GateAssignment, FlightStatusHistory
from .serializers import FlightSerializer, GateAssignmentSerializer, FlightStatusHistorySerializer
from users.permissions import IsAirportAdmin, IsOperator

class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated, IsAirportAdmin]

class GateAssignmentViewSet(ModelViewSet):
    queryset = GateAssignment.objects.all()
    serializer_class = GateAssignmentSerializer
    permission_classes = [IsAuthenticated, IsAirportAdmin]

class FlightStatusHistoryViewSet(ModelViewSet):
    queryset = FlightStatusHistory.objects.all()
    serializer_class = FlightStatusHistorySerializer
    permission_classes = [IsAuthenticated, IsOperator]
