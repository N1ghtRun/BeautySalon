import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from services.models import Service as ServiceModel, Calendar as CalendarModel, Master as MasterModel


class ServiceList(ListView):
    model = ServiceModel
    template_name = 'services.html'
    context_object_name = 'services'


class ServiceDetail(DetailView):
    model = ServiceModel
    template_name = 'service.html'
    context_object_name = 'service'


def root(request):
    calendars = CalendarModel.objects.filter(date__gte=datetime.date.today(),
                                             date__lte=datetime.date.today() + datetime.timedelta(days=7)).all()
    masters = MasterModel.objects.filter(calendar__in=calendars).distinct()
    services = ServiceModel.objects.filter(master__in=masters).distinct()

    return render(request, 'index.html', {'services': list(services)})


def service_single(request, service_name):
    return HttpResponse('Single service page')


def specialist(request):
    return HttpResponse('Specialists page')


def specialist_single(request, specialist_id):
    return HttpResponse('Single specialist page')
