from django import forms
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
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
            'status': forms.HiddenInput(),
        }
