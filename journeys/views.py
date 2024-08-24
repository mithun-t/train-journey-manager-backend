from rest_framework import viewsets
from .models import TrainJourney, Station, Status, Berth, PaymentMode
from .serializers import TrainJourneySerializer, StationSerializer, StatusSerializer, BerthSerializer, PaymentModeSerializer


class TrainJourneyViewSet(viewsets.ModelViewSet):
    queryset = TrainJourney.objects.all()
    serializer_class = TrainJourneySerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class BerthViewSet(viewsets.ModelViewSet):
    queryset = Berth.objects.all()
    serializer_class = BerthSerializer

class PaymentModeViewSet(viewsets.ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer
