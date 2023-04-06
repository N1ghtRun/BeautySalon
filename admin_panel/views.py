from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from services.models import Service as ServiceModel, Specialist as SpecialistModel, WorkSchedule as WorkScheduleModel


def panel(request):
    return render(request, 'admin_panel/panel.html')


def services(request):
    services = ServiceModel.objects.all()
    if request.method == 'POST':
        new_service = ServiceModel(name=request.POST.get('name'), time=request.POST.get('time'),
                                   price=request.POST.get('price'))
        new_service.save()

    return render(request, 'admin_panel/services.html', {'services': services})


def service_single(request, service_id):
    service = ServiceModel.objects.get(id=service_id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.time = request.POST.get('time')
        service.price = request.POST.get('price')
        service.save()
    return render(request, 'service.html', {'service': service})


def specialists(request):
    if request.method == 'POST':
        new_specialist = SpecialistModel(name=request.POST.get('name'), rank=request.POST.get('rank'),
                                         phone=request.POST.get('phone'), status=request.POST.get('status'))
        new_specialist.save()

        service_ids = [value for key, value in request.POST.items() if key.startswith('service')]
        for service_id in service_ids:
            service = ServiceModel.objects.get(id=service_id)
            new_specialist.services.add(service)

    services = ServiceModel.objects.all()
    specialists = SpecialistModel.objects.all()

    return render(request, 'admin_panel/specialists.html', {'services': services, 'specialists': specialists})


def specialist_single(request, specialist_id):
    specialist = SpecialistModel.objects.get(id=specialist_id)
    services = ServiceModel.objects.all()

    if request.method == 'POST':
        specialist.name = request.POST.get('name')
        specialist.rank = request.POST.get('rank')
        specialist.phone = request.POST.get('phone')
        specialist.status = request.POST.get('status')
        specialist.save()

    return render(request, 'admin_panel/specialist.html', {'specialist': specialist, 'services': services})


def specialist_schedule(request, specialist_id):
    specialist = SpecialistModel.objects.get(id=specialist_id)
    schedules = WorkScheduleModel.objects.filter(specialist_id=specialist_id)

    if request.method == 'POST':
        new_schedule = WorkScheduleModel(specialist=specialist, date=request.POST.get('date'),
                                     time_start=request.POST.get('time_start'),
                                     time_end=request.POST.get('time_end'))
        new_schedule.save()

    return render(request, 'admin_panel/specialist_schedule.html', {'schedules': schedules, 'specialist': specialist})


def specialist_schedule_single(request, specialist_id, schedule_id):
    schedule = WorkScheduleModel.objects.get(id=schedule_id)
    if request.method == 'POST':
        schedule.date = request.POST.get('date')
        schedule.time_start = request.POST.get('time_start')
        schedule.time_end = request.POST.get('time_end')
        schedule.save()

    return render(request, 'admin_panel/specialist_schedule_single.html', {'schedule': schedule})


def bookings(request):
    return HttpResponse('Bookings')
