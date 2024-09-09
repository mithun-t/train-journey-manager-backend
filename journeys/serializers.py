from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TrainJourney, Station, Train, Status, Berth, PaymentMode

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TrainJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainJourney
        fields = '__all__'
        read_only_fields = ('user',)

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'code', 'name']
        read_only_fields = ('user',)

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'code', 'name']
        read_only_fields = ('user',)

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'code', 'name']
        read_only_fields = ('user',)

class BerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berth
        fields = ['id', 'code', 'name']
        read_only_fields = ('user',)

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = ['id', 'code', 'name']
        read_only_fields = ('user',)
