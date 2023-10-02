import datetime


# Sets default for 'date' field as tomorrow
date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)


# Defines options for booking times (12.00 to 9.45pm)

TIMES = tuple()
time_list = list(TIMES)

for h in range(12, 22):
    for m in range(0, 60, 15):
        if m == 0:
            t_text = f'{h}:00'
        else:
            t_text = f'{h}:{m}'

        t_val = datetime.time(h, m)
        time_list.append((t_val, t_text))

TIMES = tuple(time_list)


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
