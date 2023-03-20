from django.shortcuts import render
from django.http import HttpResponse


def panel(request):
    return HttpResponse('Admin panel')


def bookings(request):
    return HttpResponse('Bookings')


def specialist(request):
    return HttpResponse('Specialists')


def specialist_single(request, specialist_id):
    return HttpResponse('Single specialist')
