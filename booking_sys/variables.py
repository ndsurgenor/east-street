import datetime

# Sets default for 'date' field as tomorrow
date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)


# Defines options for booking times (12.00 to 9.45pm)
TIMES = tuple()
time_list = list(TIMES)

for hrs in range(12, 22):
    for min in range(0, 60, 15):
        if min == 0:
            time_text = f'{hrs}:00'
        else:
            time_text = f'{hrs}:{min}'

        time_val = datetime.time(hrs, min)
        time_list.append((time_val, time_text))

TIMES = tuple(time_list)


# Defines options for size of booking party (min=1, max=12)
GROUP_SIZE = tuple()

for num in range(1, 13):
    GROUP_SIZE += ((num, str(num)),)


# Allows admin to confirm/deny user bookings
STATUS = (
    (0, 'Booking Requested'),
    (1, 'Booking Confirmed'),
    (2, 'Booking Cancelled'),
)
