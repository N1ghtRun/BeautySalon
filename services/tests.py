from django.test import TestCase, Client

from services.models import Service as ServiceModel, Specialist as SpecialistModel, Booking as BookingModel


class Test(TestCase):
    fixtures = ['fixture_test.json']

    def test_booking(self):
        service = ServiceModel.objects.get(id=1)
        specialist = SpecialistModel.objects.get(id=1)

        services = ServiceModel.objects.all()
        specialists = SpecialistModel.objects.all()
        bookings = BookingModel.objects.all()

        c = Client()
        c.login(username='admin', password='admin')
        response = c.post('/booking/',
                          {'services': services, 'specialists': specialists, 'bookings': bookings,
                           'specialist': f'{specialist.id}',
                           'service': f'{service.id}',
                           'date_time': '2023-04-11|08:00:00'})
        self.assertEqual(response.status_code, 200)

        bookings = BookingModel.objects.all()
        self.assertEqual(len(bookings), 9)
