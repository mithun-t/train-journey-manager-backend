from rest_framework import viewsets
from .models import TrainJourney
from .serializers import TrainJourneySerializer

class TrainJourneyViewSet(viewsets.ModelViewSet):
    queryset = TrainJourney.objects.all()
    serializer_class = TrainJourneySerializer
