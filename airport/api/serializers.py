from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from airport.api.models import Airport, Aircraft, AircraftTypes, Passenger, Flight, Ticket


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AircraftTypesSerializer(ModelSerializer):
    class Meta:
        model = AircraftTypes
        fields = '__all__'


class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'