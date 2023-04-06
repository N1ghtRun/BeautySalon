from datetime import timedelta
from services import models


def convert_periods_to_set(time_start, time_end):
    time_set = set()
    while time_start <= time_end:
        time_set.add(time_start)
        time_start += timedelta(minutes=15)

    return time_set


def calc_free_time_in_day(specialist, service, workday_time_start, workday_time_end):
    free_time = []
    bookings = models.Booking.objects.filter(specialist=specialist, date__day=workday_time_start.day)
    busy_time = []
    for booking in bookings:
        booking_time_start = booking.date
        booking_time_end = booking.date + timedelta(minutes=booking.service.time)
        busy_time.append(
            convert_periods_to_set(booking_time_start.replace(tzinfo=None), booking_time_end.replace(tzinfo=None)))

    day_times = convert_periods_to_set(workday_time_start, workday_time_end - timedelta(minutes=service.time))

    for time_start in day_times:
        possible_time = convert_periods_to_set(time_start, time_start + timedelta(minutes=service.time))
        print(service.time)
        no_intersections = True
        for one_booking in busy_time:
            if len(possible_time.intersection(one_booking)) > 1:
                no_intersections = False
        if no_intersections:
            free_time.append(time_start)

    return free_time
