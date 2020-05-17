from django.db import models


class AircraftTypes(models.Model):
    type = models.CharField(max_length=50, blank=False, default="")


class Aircraft(models.Model):
    type = models.ForeignKey(AircraftTypes, on_delete=models.CASCADE, related_name="aircraft", null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False, default="")
    seats = models.IntegerField()


class Airport(models.Model):
    location = models.CharField(max_length=150, blank=False, default="")
    name = models.CharField(max_length=180, blank=False, default="")
    rating = models.FloatField()
    icaoCode = models.CharField(max_length=10, default='')

    class Meta:
        ordering = ['name']


class Flight(models.Model):
    flightNumber = models.CharField(max_length=15, blank=False, default="")
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airports', blank=False)
    aircraft = models.ForeignKey(AircraftTypes,on_delete=models.CASCADE, related_name='flight',  blank=False)
    departureDateTime = models.DateTimeField(null=False)
    arrivalDateTime = models.DateTimeField(null=False)
    toWhere = models.CharField(max_length=120, blank=False, default="")


class Passenger(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')


class Ticket(models.Model):
    number = models.CharField(max_length=40, blank=False, default="", primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='ticket', null=False, blank=False)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='ticket', null=False, blank=False)
    seatNum = models.IntegerField()
