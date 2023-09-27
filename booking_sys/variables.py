import datetime

# Defines times allowed for bookings (start 12:00pm, end 9.30pm)
DATES = (
    (datetime.date(2023, 9, 1), '01/09/23'),
    (datetime.date(2023, 9, 2), '02/09/23'),
    (datetime.date(2023, 9, 3), '03/09/23'),
    (datetime.date(2023, 9, 4), '04/09/23'),
    (datetime.date(2023, 9, 5), '05/09/23'),
    (datetime.date(2023, 9, 6), '06/09/23'),
    (datetime.date(2023, 9, 7), '07/09/23'),
    (datetime.date(2023, 9, 8), '08/09/23'),
    (datetime.date(2023, 9, 9), '09/09/23'),
    (datetime.date(2023, 9, 10), '10/09/23'),
    (datetime.date(2023, 9, 11), '11/09/23'),
    (datetime.date(2023, 9, 12), '12/09/23'),
    (datetime.date(2023, 9, 13), '13/09/23'),
    (datetime.date(2023, 9, 14), '14/09/23'),
    (datetime.date(2023, 9, 15), '15/09/23'),
    (datetime.date(2023, 9, 16), '16/09/23'),
)

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
GROUP_SIZE = tuple()

for i in range(1, 13):
    GROUP_SIZE += ((i, str(i)),)


# Allows admin to confirm/deny user bookings
STATUS = (
    (0, 'Booking Requested'),
    (1, 'Booking Confirmed'),
    (2, 'Booking Cancelled'),
)
