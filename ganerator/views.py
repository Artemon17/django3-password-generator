from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "ganerator/home.html")


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend('abcdefghijklmnopqrstuvwxyz'.upper())
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*_-":><.,{}][+=')
    lenght = int(request.GET.get('lenght', 9))
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, "ganerator/password.html", {'password': thepassword})


def description(request):
    return render(request, 'ganerator/description.html')