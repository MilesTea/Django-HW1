from django.http import HttpResponse
from django.shortcuts import render, reverse
import time
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse("time"),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = time.strftime('%H:%M:%S', time.localtime())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = 'Список файлов и директорий:'
    for thing in os.listdir():
        msg += '<br>' + thing
    return HttpResponse(msg)
