from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Booking


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def location(request):
    return render(request, 'location.html')


class UserBookings(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=0).order_by('date')
    template_name = 'userbookings.html'
    paginate_by = 10
