from django.contrib import admin

from .models import AircraftTypes, Aircraft, Ticket, Passenger, Airport, Flight

admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(AircraftTypes)
admin.site.register(Ticket)
admin.site.register(Passenger)
