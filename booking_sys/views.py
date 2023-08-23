from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Booking


def index(request):
    return render(request, 'index.html')


class UserBookings(generic.ListView):
    model = Booking
    template_name = 'bookings.html'
