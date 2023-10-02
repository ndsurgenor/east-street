import datetime


# Sets default for 'date' field as tomorrow
date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)


# Defines options for booking times (12.00 to 9.45pm)
TIMES = (
    (datetime.time(12, 0), '12:00pm'),
    (datetime.time(12, 15), '12:15pm'),
    (datetime.time(12, 30), '12:30pm'),
    (datetime.time(12, 45), '12:45pm'),
    (datetime.time(13, 0), '1:00pm'),
    (datetime.time(13, 15), '1:15pm'),
    (datetime.time(13, 30), '1:30pm'),
    (datetime.time(13, 45), '1:45pm'),
    (datetime.time(14, 0), '2:00pm'),
    (datetime.time(14, 15), '2:15pm'),
    (datetime.time(14, 30), '2:30pm'),
    (datetime.time(14, 45), '2:45pm'),
    (datetime.time(15, 0), '3:00pm'),
    (datetime.time(15, 15), '3:15pm'),
    (datetime.time(15, 30), '3:30pm'),
    (datetime.time(15, 45), '3:45pm'),
    (datetime.time(16, 0), '4:00pm'),
    (datetime.time(16, 15), '4:15pm'),
    (datetime.time(16, 30), '4:30pm'),
    (datetime.time(16, 45), '4:45pm'),
    (datetime.time(17, 0), '5:00pm'),
    (datetime.time(17, 15), '5:15pm'),
    (datetime.time(17, 30), '5:30pm'),
    (datetime.time(17, 45), '5:45pm'),
    (datetime.time(18, 0), '6:00pm'),
    (datetime.time(18, 15), '6:15pm'),
    (datetime.time(18, 30), '6:30pm'),
    (datetime.time(18, 45), '6:45pm'),
    (datetime.time(19, 0), '7:00pm'),
    (datetime.time(19, 15), '7:15pm'),
    (datetime.time(19, 30), '7:30pm'),
    (datetime.time(19, 45), '7:45pm'),
    (datetime.time(20, 0), '8:00pm'),
    (datetime.time(20, 15), '8:15pm'),
    (datetime.time(20, 30), '8:30pm'),
    (datetime.time(20, 45), '8:45pm'),
    (datetime.time(21, 0), '9:00pm'),
    (datetime.time(21, 15), '9:15pm'),
    (datetime.time(21, 30), '9:30pm'),
    (datetime.time(21, 45), '9:45pm'),
)


# Defines options for size of booking party (min=1, max=12)
GROUP_SIZE = tuple()

for i in range(1, 13):
    GROUP_SIZE += ((i, str(i)),)


# Allows admin to confirm/deny user bookings
STATUS = (
    (0, 'Booking Requested'),
    (1, 'Booking Confirmed'),
    (2, 'Booking Cancelled'),
)
