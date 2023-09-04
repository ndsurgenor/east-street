from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def location(request):
    return render(request, 'location.html')


class UserBookings(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'userbookings.html'
    paginate_by = 10


class BookingDetail(View):

    def get(self, request, reference, *args, **kwargs):
        queryset = Booking.objects
        booking = get_object_or_404(queryset, slug=reference)

    return render(
        request,
        'userbookings.html',
        {
            'booking': booking,
        },
    )
