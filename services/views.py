import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from services.models import Service as ServiceModel, WorkSchedule as WorkScheduleModel, Specialist as SpecialistModel, \
    Booking as BookingModel
from services.utils.periods_calc import calc_free_time_in_day


def root(request):
    work_schedules = WorkScheduleModel.objects.filter(date__gte=datetime.date.today(),
                                                      date__lte=datetime.date.today() + datetime.timedelta(
                                                          days=7)).all()
    masters = SpecialistModel.objects.filter(workschedule__in=work_schedules).distinct()
    services = ServiceModel.objects.filter(specialist__in=masters).distinct()

    return render(request, 'index.html', {'services': list(services)})


def services(request):
    services = ServiceModel.objects.all()

    return render(request, 'services.html', {'services': services})


@login_required(login_url='login')
def service_single(request, service_id):
    work_schedules = WorkScheduleModel.objects.filter(date__gte=datetime.date.today(),
                                                      date__lte=datetime.date.today() + datetime.timedelta(
                                                          days=7)).all()
    service = ServiceModel.objects.get(id=service_id)
    specialists = SpecialistModel.objects.filter(workschedule__in=work_schedules, services__id=service_id)

    return render(request, 'service.html', {'service': service, 'specialists': specialists})


def specialists(request):
    services = ServiceModel.objects.all()
    specialists = SpecialistModel.objects.all()

    return render(request, 'specialists.html', {'services': services, 'specialists': specialists})


@login_required(login_url='login')
def specialist_single(request, specialist_id):
    work_schedules = WorkScheduleModel.objects.filter(date__gte=datetime.date.today(),
                                                      date__lte=datetime.date.today() + datetime.timedelta(
                                                          days=7)).all()
    specialist = SpecialistModel.objects.get(id=specialist_id)
    services = ServiceModel.objects.filter(specialist__id=specialist_id)

    return render(request, 'specialist.html', {'specialist': specialist, 'services': services})


@login_required(login_url='login')
def booking(request):
    work_schedules = WorkScheduleModel.objects.filter(date__gte=datetime.date.today(),
                                                      date__lte=datetime.date.today() + datetime.timedelta(
                                                          days=7)).all()
    specialists = SpecialistModel.objects.filter(workschedule__in=work_schedules).distinct()
    services = ServiceModel.objects.filter(specialist__in=specialists).distinct()

    client = User.objects.get(id=request.user.pk)
    # client = User.objects.get(id=1)
    bookings = BookingModel.objects.all()

    if request.method == 'POST':
        specialist_single = SpecialistModel.objects.get(id=request.POST.get('specialist'))
        service_single = ServiceModel.objects.get(id=request.POST.get('service'))
        new_booking = BookingModel(specialist=specialist_single, service=service_single,
                                   client=client, date=request.POST.get('date_time'), status=True)

        appointment_date = request.POST.get('date_time')
        appointment_date_obj = datetime.datetime.fromisoformat(appointment_date.replace("Z", "+00:00"))
        schedule_obj = WorkScheduleModel.objects.filter(date=appointment_date_obj.date(), specialist=specialist_single)
        time_start = schedule_obj[0].time_start
        time_end = schedule_obj[0].time_end
        time_start_date = datetime.datetime.combine(appointment_date_obj.date(), time_start)
        time_end_date = datetime.datetime.combine(appointment_date_obj.date(), time_end)
        bookings_day = BookingModel.objects.filter(specialist=specialist_single, date__day=time_start_date.day)
        free_time = calc_free_time_in_day(bookings_day, service_single, time_start_date, time_end_date)
        if appointment_date_obj in free_time:
            new_booking.save()
        else:
            return HttpResponse('Wrong time')

    # paginator
    paginator = Paginator(bookings, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'booking.html', {'specialists': specialists, 'services': services, 'page_obj': page_obj})