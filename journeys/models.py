from django.db import models
from django.contrib.auth.models import User

class TrainJourney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journey_date = models.DateField()
    train_number = models.CharField(max_length=10)
    departure_station = models.CharField(max_length=100)
    arrival_station = models.CharField(max_length=100)
    pnr_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    berth = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    booked_date = models.DateField()
    bill_date = models.DateField()
    payment_mode = models.CharField(max_length=50)
    journey_status = models.CharField(max_length=50)

class Train(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Station(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Berth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class PaymentMode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.nameex
