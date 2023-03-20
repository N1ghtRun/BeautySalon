from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return HttpResponse('User')


def booking(request):
    return HttpResponse('User/Booking')
