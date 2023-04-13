from django.test import TestCase, Client
from services.models import Service, Specialist, Booking


class Test(TestCase):
    def test_service(self):
        c = Client()
        response = c.post('/panel/services/', {'name': 'testservice', 'time': 1, 'price': 1})
        self.assertEqual(response.status_code, 200)

        service = Service(name='testservice2', time=1, price=1)
        service.save()
        all_services = Service.objects.all()

        self.assertEqual(len(all_services), 2)

    def test_specialist(self):
        service = Service(name='testservice', time=1, price=1)
        service.save()

        c = Client()
        response = c.post('/panel/specialists/',
                          {'name': 'Anna', 'status': 1, 'rank': 1, 'phone': 1234567890,
                           f'service_{service.id}': service.id})
        self.assertEqual(response.status_code, 200)

    def test_specialist_schedule(self):
        service = Service(name='test_schedule', time=30, price=200)
        service.save()
        specialist = Specialist(name='Anna', phone=123456789, status=1, rank=1)
        specialist.save()
        specialist.services.add(service)
        client = Client()
        response = client.post(f'/panel/specialist/{specialist.id}/schedule/',
                               {'specialist': specialist, 'date': '2024-04-12', 'time_start': '12:00',
                                'time_end': '13:00'})

        self.assertEqual(response.status_code, 200)
