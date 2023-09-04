from django.db import models
from django.contrib.auth.models import User
from .variables import TIMES, GROUP_SIZE, STATUS


class Booking(models.Model):
    """
    Model for user-made booking
    """
    reference = models.SlugField(max_length=20, unique=True)
    contact = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField(choices=TIMES)
    group = models.IntegerField(choices=GROUP_SIZE, default=1)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.reference
