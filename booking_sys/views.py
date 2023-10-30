from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Booking
from .forms import BookingForm


# Static views for main site

def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def location(request):
    return render(request, 'location.html')


# Class views for booking site

class BookFormView(generic.CreateView):
    """
    View to create a new booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = '/bookinglist'

    def form_valid(self, form):
        form.instance.contact_id = self.request.user.id
        messages.success(self.request, 'Booking submitted successfully')
        return super(BookFormView, self).form_valid(form)


class BookListView(generic.ListView):
    """
    View to display bookings already made by a user
    """
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'bookinglist.html'


class BookUpdateView(UserPassesTestMixin, generic.UpdateView):
    """
    View to allow a booking to be updated
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = '/bookinglist'

    def test_func(self):
        return self.request.user.id == self.get_object().contact_id

    def form_valid(self, form):
        form.instance.status = 0
        messages.success(self.request, 'Booking updated successfully')
        return super(BookUpdateView, self).form_valid(form)


class BookDeleteView(generic.DeleteView):
    """
    View to allow deletion of a booking
    """
    model = Booking
    template_name = 'bookingdelete.html'
    success_url = '/bookinglist'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking deleted successfully')
        return super(BookDeleteView, self).delete(request, *args, **kwargs)
