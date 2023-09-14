from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


# Static views for main site
def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def location(request):
    return render(request, 'location.html')


# Generates a booking form for the user
class BookFormView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = '/userbookings'

    def form_valid(self, form):
        form.instance.contact_id = self.request.user.id
        return super(BookFormView, self).form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            print(f"Field: {field}")
            for error in errors:
                print(f"Error: {error}")
        return HttpResponse(f'Form invalid')


# Generates a list of the user's bookings
class BookListView(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'userbookings.html'


# Allows a user to update a booking
class BookUpdateView(generic.UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = '/userbookings'

    def form_valid(self, form):
        # form.instance.contact_id = self.request.user.id
        messages.success(self.request, 'The booking was successfully updated')
        return super(BookUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            print(f"Field: {field}")
            for error in errors:
                print(f"Error: {error}")
        return HttpResponse(f'Form invalid')


# Allows a user to delete a booking
class BookDeleteView(generic.DeleteView):
    model = Booking
    template_name = 'bookingdelete.html'
    success_url = '/userbookings'
