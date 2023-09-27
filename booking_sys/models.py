from django.db import models
from django.contrib.auth.models import User
from .variables import GROUP_SIZE, STATUS


class Booking(models.Model):
    """
    Model for user-made booking
    """
    contact = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    group = models.IntegerField(choices=GROUP_SIZE, default=2)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f'{self.date}, {self.time} - {self.contact} x{self.group}'
