from django import forms
from django.contrib.auth.models import User
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to allow user-made bookings
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'group', 'status')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.HiddenInput(),
        }
