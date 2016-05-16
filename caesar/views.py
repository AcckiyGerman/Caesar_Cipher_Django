from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def encode(request):
    inputText = request.GET['inputText']
    rotate = request.GET['rotate']
    # HERE SOME MODEL WORK
    data = {
        'outputText': inputText,
        'frequencyDict': 'frequencyDict',
        'unravelText': 'unravelText'
    }
    jsonData = json.dumps(data)
    return HttpResponse(jsonData, content_type='application/json')


def decode(request):
    return HttpResponse('decoded text')