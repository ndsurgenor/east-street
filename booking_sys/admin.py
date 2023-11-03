from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ['contact', 'date', 'time', 'group']


admin.site.register(Booking)
