from django.test import TestCase, Client
import datetime

from services.models import Service as ServiceModel, Specialist as SpecialistModel, Booking as BookingModel, \
    WorkSchedule as ScheduleModel
from django.contrib.auth.models import User


class Test(TestCase):
    fixtures = ['fixture_test.json']

    def test_booking(self):

        service_1 = ServiceModel(name='test_service_1', time=30, price=200)
        service_1.save()
        specialist = SpecialistModel(name='Anna', phone=123456789, status=1, rank=1)
        specialist.save()
        specialist.services.add(service_1)
        user = User(username='admin2')
        user.set_password('admin2')
        user.save()
        schedule = ScheduleModel(specialist=specialist, date=datetime.date(year=2017, month=2, day=15),
                                 time_start=datetime.time(hour=8, minute=0), time_end=datetime.time(hour=15, minute=0))
        # schedule = ScheduleModel(specialist=specialist, date='2017-02-15', time_start='8:00', time_end='15:00')
        schedule.save()

        services = ServiceModel.objects.all()
        specialists = SpecialistModel.objects.all()
        bookings = BookingModel.objects.all()


        c = Client()
        c.login(username='admin', password='admin')
        response = c.post('/booking/',
                          {'services': services, 'specialists': specialists, 'bookings': bookings,
                           'specialist': f'{specialist.id}',
                           'service': f'{service_1.id}',
                           'date_time': '2017-02-15|09:00:00'})
        self.assertEqual(response.status_code, 200)

        bookings = BookingModel.objects.all()
        self.assertEqual(len(bookings), 9)


# from services.utils.periods_calc import convert_periods_to_set, test_calc_free_time_in_day

#
# class Test(TestCase):
#     def test_convert_periods_to_set(self):
#         time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         time_end = datetime.datetime(2023, 4, 7, 9, 0)
#         result = convert_periods_to_set(time_start, time_end)
#         expected_result = {
#             datetime.datetime(2023, 4, 7, 8, 0),
#             datetime.datetime(2023, 4, 7, 8, 15),
#             datetime.datetime(2023, 4, 7, 8, 30),
#             datetime.datetime(2023, 4, 7, 8, 45),
#             datetime.datetime(2023, 4, 7, 9, 0)
#         }
#         self.assertSetEqual(result, expected_result)
#
#     def test_string_convert_periods_to_set(self):
#         time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         time_end = 'test'
#
#         with self.assertRaises(TypeError):
#             convert_periods_to_set(time_start, time_end)
#
#     def test_reverse_convert_periods_to_set(self):
#         time_end = datetime.datetime(2023, 4, 7, 8, 0)
#         time_start = datetime.datetime(2023, 4, 7, 9, 0)
#         result = convert_periods_to_set(time_start, time_end)
#         expected_result = set()
#         self.assertSetEqual(result, expected_result)
#
#     def test_same_reverse_convert_periods_to_set(self):
#         time_end = datetime.datetime(2023, 4, 7, 8, 0)
#         time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         result = convert_periods_to_set(time_start, time_end)
#         expected_result = {datetime.datetime(2023, 4, 7, 8, 0)}
#         self.assertSetEqual(result, expected_result)
#
#     def test_calc_free_time_in_day(self):
#         booking = [{
#             'date': datetime.datetime(2023, 4, 7, 8, 0),
#             'service_time': 30,
#         }]
#         service_time = 30
#         workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         workday_time_end = datetime.datetime(2023, 4, 7, 9, 0)
#         result = test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end)
#         expected_result = [datetime.datetime(2023, 4, 7, 8, 30)]
#         self.assertListEqual(result, expected_result)
#
#         # second test
#         workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         workday_time_end = datetime.datetime(2023, 4, 7, 10, 0)
#         result = set(test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end))
#         expected_result = {datetime.datetime(2023, 4, 7, 8, 30), datetime.datetime(2023, 4, 7, 8, 45),
#                            datetime.datetime(2023, 4, 7, 9, 0), datetime.datetime(2023, 4, 7, 9, 15),
#                            datetime.datetime(2023, 4, 7, 9, 30)}
#         self.assertSetEqual(result, expected_result)
#
#         # third test
#         booking = [{
#             'date': datetime.datetime(2023, 4, 7, 8, 0),
#             'service_time': 30,
#         },
#             {
#                 'date': datetime.datetime(2023, 4, 7, 8, 30),
#                 'service_time': 30,
#             },
#         ]
#         workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
#         workday_time_end = datetime.datetime(2023, 4, 7, 9, 0)
#         result = test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end)
#         expected_result = []
#         self.assertListEqual(result, expected_result)
