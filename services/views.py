from django.shortcuts import render
from django.http import HttpResponse


def root(request):
    return HttpResponse('Main page')


def service_single(request, service_name):
    return HttpResponse('Single service page')


def specialist(request):
    return HttpResponse('Specialists page')


def specialist_single(request, specialist_id):
    return HttpResponse('Single specialist page')
