from django.db import models
from django.contrib.auth.models import User

# Defines options for size of booking party (min=1, max=12)
GROUP_SIZE = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
)

# Allows admin to confirm/deny user bookings
STATUS = (
    (0, 'Request sent to restaurant'),
    (1, 'Booking confirmed by restaurant')
)


class Booking(models.Model):
    """
    Model for User made booking
    """
    reference = models.SlugField(max_length=12, unique=True)
    contact = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    group = models.IntegerField(choices=GROUP_SIZE, default=1)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.title
