import datetime

# Defines times allowed for bookings (start 12:00pm, end 9.30pm)
TIMES = (
    (datetime.time(12, 00), '12:00pm'),
    (datetime.time(12, 15), '12:15pm'),
    (datetime.time(12, 30), '12:30pm'),
    (datetime.time(12, 45), '12:45pm'),
    (datetime.time(13, 00), '1:00pm'),
    (datetime.time(13, 15), '1:15pm'),
    (datetime.time(13, 30), '1:30pm'),
    (datetime.time(13, 45), '1:45pm'),
    (datetime.time(14, 00), '2:00pm'),
    (datetime.time(14, 15), '2:15pm'),
    (datetime.time(14, 30), '2:30pm'),
    (datetime.time(14, 45), '2:45pm'),
    (datetime.time(15, 00), '3:00pm'),
    (datetime.time(15, 15), '3:15pm'),
    (datetime.time(15, 30), '3:30pm'),
    (datetime.time(15, 45), '3:45pm'),
)

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
    (0, 'Booking Requested'),
    (1, 'Booking Confirmed')
)
