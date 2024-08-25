from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import TrainJourney, Station, Status, Berth, PaymentMode
from .serializers import TrainJourneySerializer, StationSerializer, StatusSerializer, BerthSerializer, PaymentModeSerializer, UserSerializer

class TrainJourneyViewSet(viewsets.ModelViewSet):
    serializer_class = TrainJourneySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TrainJourney.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

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
