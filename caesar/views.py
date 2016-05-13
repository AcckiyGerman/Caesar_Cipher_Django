from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def encode(request):
    return HttpResponse('encoded text')


def decode(request):
    return HttpResponse('decoded text')