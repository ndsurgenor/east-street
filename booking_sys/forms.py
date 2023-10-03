from django import forms
from .models import Booking
import datetime


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

    def clean_date(self):
        date = self.cleaned_data['date']
        if date <= datetime.date.today():
            raise forms.ValidationError(
                "A booking cannot be made any earlier than tomorrow")
        if date.weekday() == 0:
            raise forms.ValidationError(
                "Sorry, the restaurant is closed on a Monday")
        if date.weekday() == 1:
            raise forms.ValidationError(
                "Sorry, the restaurant is closed on a Tuesday")
        return date
