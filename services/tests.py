from django.test import TestCase

import datetime
from services.utils.periods_calc import convert_periods_to_set, test_calc_free_time_in_day


class Test(TestCase):
    def test_convert_periods_to_set(self):
        time_start = datetime.datetime(2023, 4, 7, 8, 0)
        time_end = datetime.datetime(2023, 4, 7, 9, 0)
        result = convert_periods_to_set(time_start, time_end)
        expected_result = {
            datetime.datetime(2023, 4, 7, 8, 0),
            datetime.datetime(2023, 4, 7, 8, 15),
            datetime.datetime(2023, 4, 7, 8, 30),
            datetime.datetime(2023, 4, 7, 8, 45),
            datetime.datetime(2023, 4, 7, 9, 0)
        }
        self.assertSetEqual(result, expected_result)

    def test_string_convert_periods_to_set(self):
        time_start = datetime.datetime(2023, 4, 7, 8, 0)
        time_end = 'test'

        with self.assertRaises(TypeError):
            convert_periods_to_set(time_start, time_end)

    def test_reverse_convert_periods_to_set(self):
        time_end = datetime.datetime(2023, 4, 7, 8, 0)
        time_start = datetime.datetime(2023, 4, 7, 9, 0)
        result = convert_periods_to_set(time_start, time_end)
        expected_result = set()
        self.assertSetEqual(result, expected_result)

    def test_same_reverse_convert_periods_to_set(self):
        time_end = datetime.datetime(2023, 4, 7, 8, 0)
        time_start = datetime.datetime(2023, 4, 7, 8, 0)
        result = convert_periods_to_set(time_start, time_end)
        expected_result = {datetime.datetime(2023, 4, 7, 8, 0)}
        self.assertSetEqual(result, expected_result)

    def test_calc_free_time_in_day(self):
        booking = [{
            'date': datetime.datetime(2023, 4, 7, 8, 0),
            'service_time': 30,
        }]
        service_time = 30
        workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
        workday_time_end = datetime.datetime(2023, 4, 7, 9, 0)
        result = test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end)
        expected_result = [datetime.datetime(2023, 4, 7, 8, 30)]
        self.assertListEqual(result, expected_result)

        # second test
        workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
        workday_time_end = datetime.datetime(2023, 4, 7, 10, 0)
        result = set(test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end))
        expected_result = {datetime.datetime(2023, 4, 7, 8, 30), datetime.datetime(2023, 4, 7, 8, 45),
                           datetime.datetime(2023, 4, 7, 9, 0), datetime.datetime(2023, 4, 7, 9, 15),
                           datetime.datetime(2023, 4, 7, 9, 30)}
        self.assertSetEqual(result, expected_result)

        # third test
        booking = [{
            'date': datetime.datetime(2023, 4, 7, 8, 0),
            'service_time': 30,
        },
            {
                'date': datetime.datetime(2023, 4, 7, 8, 30),
                'service_time': 30,
            },
        ]
        workday_time_start = datetime.datetime(2023, 4, 7, 8, 0)
        workday_time_end = datetime.datetime(2023, 4, 7, 9, 0)
        result = test_calc_free_time_in_day(booking, service_time, workday_time_start, workday_time_end)
        expected_result = []
        self.assertListEqual(result, expected_result)
