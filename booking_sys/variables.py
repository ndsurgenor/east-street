# Defines times allowed for bookings (start 12:00pm, end 9.30pm)
TIMES = (
    (1, '12:00pm'),
    (2, '12:15pm'),
    (3, '12:30pm'),
    (4, '12:45pm'),
    (5, '1:00pm'),
    (6, '1:15pm'),
    (7, '1:30pm'),
    (8, '1:45pm'),
    (9, '2:00pm'),
    (10, '2:15pm'),
    (11, '2:30pm'),
    (12, '2:45pm'),
    (13, '3:00pm'),
    (14, '3:15pm'),
    (15, '3:30pm'),
    (16, '3:45pm'),
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