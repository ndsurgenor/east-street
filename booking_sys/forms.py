from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    """
    Creates calendar for date widget below
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    Creates format for time widget below
    """
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """
    Form to allow user-made bookings
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'group')
        widgets = {
            'date': DateInput,
            'time': TimeInput,
        }
