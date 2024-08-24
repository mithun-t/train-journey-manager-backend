from rest_framework import serializers
from .models import TrainJourney, Station, Status, Berth, PaymentMode

class TrainJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainJourney
        fields = '__all__' 


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'code', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'code', 'name']

class BerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berth
        fields = ['id', 'code', 'name']

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = ['id', 'code', 'name']
