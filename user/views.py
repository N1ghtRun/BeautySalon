from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def user_page(request):
    return render(request, 'user/user_page.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        if user.save():
            return redirect('login')

    return render(request, 'user/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return render(request, 'index.html')
            return redirect('index')
        else:
            return render(request, 'user/login.html', {'error': 'Wrong username or password'})

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def booking(request):
    return HttpResponse('User/Booking')
