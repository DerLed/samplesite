#from django.shortcuts import render
from django.http import HttpResponse

from .models import Bb

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plan; charset=utf-8')

def index1(request):
    return HttpResponse("<h1>Фыва.</h1>")
# Create your views here.
