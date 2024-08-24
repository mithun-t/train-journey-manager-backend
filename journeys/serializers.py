from rest_framework import serializers
from .models import TrainJourney

class TrainJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainJourney
        fields = '__all__' 
