from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'asdaqweqwe'})

def password(request):

    charachters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('lenght',12))

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charachters.extend(list('!@£$%^&*(_-)'))

    if request.GET.get('numbers'):
        charachters.extend(list('1234567890'))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(charachters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
