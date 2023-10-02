from django import forms
from django.contrib.auth.models import User
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """
    Form to allow user-made bookings
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'group', 'status')
        widgets = {
            'date': DateInput(),
            'status': forms.HiddenInput(),
        }
