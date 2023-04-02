import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from services.models import Service as ServiceModel, Calendar as CalendarModel, Specialist as SpecialistModel, \
    Booking as BookingModel


def root(request):
    calendars = CalendarModel.objects.filter(date__gte=datetime.date.today(),
                                             date__lte=datetime.date.today() + datetime.timedelta(days=7)).all()
    masters = SpecialistModel.objects.filter(calendar__in=calendars).distinct()
    services = ServiceModel.objects.filter(specialist__in=masters).distinct()

    return render(request, 'index.html', {'services': list(services)})


def service_single(request, service_name):
    return HttpResponse('Single service page')


def specialist(request):
    return HttpResponse('Specialists page')


def specialist_single(request, specialist_id):
    return HttpResponse('Single specialist page')


def booking(request):
    specialists = SpecialistModel.objects.all()
    services = ServiceModel.objects.all()
    client = User.objects.get(id=1)
    bookings = BookingModel.objects.all()

    if request.method == 'POST':
        specialist_single = SpecialistModel.objects.get(id=request.POST.get('specialist'))
        service_single = ServiceModel.objects.get(id=request.POST.get('service'))
        new_booking = BookingModel(specialist=specialist_single, service=service_single,
                                   client=client, date=request.POST.get('date_time'), status=True)
        new_booking.save()

    return render(request, 'booking.html', {'specialists': specialists, 'services': services, 'bookings': bookings})
