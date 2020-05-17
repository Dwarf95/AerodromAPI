from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import AircraftTypes, Aircraft, Airports, Flight, Passenger, Ticket, Flights, Aircrafts
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .serializers \
    import AirportSerializer, \
    AircraftTypesSerializer, AircraftSerializer, FlightSerializer, PassengerSerializer, TicketSerializer

urlpatterns = [
    path('airports/', Airports.as_view(), name='airports'),
    path('airport/<int:pk>/', views.AirportDetail.as_view(), name="airport"),
    path('aircrafts/', Aircrafts.as_view(), name='aircrafts'),
    path('aircraft-types/', AircraftTypes.as_view(), name='aircraft-types'),
    path('flights/', Flights.as_view(), name='flights'),
    path('passengers/', Passenger.as_view(), name='passengers'),
    path('tickets/', Ticket.as_view(), name='tickets'),
]

urlpatterns = format_suffix_patterns(urlpatterns)