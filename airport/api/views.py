from django.shortcuts import render

from airport.api.models import Airport, Flight, Aircraft
from airport.api.serializers import UserSerializer, AirportSerializer, FlightSerializer, PassengerSerializer, \
    TicketSerializer, AircraftTypesSerializer, AircraftSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404
from json import JSONEncoder


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class Airports(ListAPIView):
    serializer_class = AirportSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Airport.objects.all()
        return queryset_list


class AirportDetail(APIView):

    def get_object(self, pk):
        try:
            return Airport.objects.get(pk=pk)
        except Airport.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        airport = self.get_object(pk)
        serializer = AirportSerializer(airport)
        return Response(serializer.data)


class Flights(ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Flight.objects.all()

        return queryset_list

    def post(self, request):
        serializer = FlightSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


class Aircrafts(ListAPIView):
    serializer_class = AircraftSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Aircraft.objects.all()

        return queryset_list


class AircraftTypes(ListAPIView):
    serializer_class = AircraftTypesSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = AircraftTypes.objects.all()

        return queryset_list


class Passenger(ListAPIView):
    serializer_class = PassengerSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Passenger.objects.all()

        return queryset_list


class Ticket(ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Ticket.objects.all()

        return queryset_list

