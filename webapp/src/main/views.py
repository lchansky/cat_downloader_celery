from django.http import HttpResponse
from django.shortcuts import render
from . import tasks

def home(request):
    tasks.download_cat.delay()
    return HttpResponse('<h1>Гружу кота!!!</h1>')

