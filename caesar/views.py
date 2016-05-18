from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Coder


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def encode(request):
    inputText, rotate = getCaesarDataFromRequest(request)
    message = Coder(inputText)
    jsonData = json.dumps({
        'outputText': message.encode(rotate),
        'frequencyDict': '',
        'unravelText': ''
    })
    return HttpResponse(jsonData, content_type='application/json')


def decode(request):
    inputText, rotate = getCaesarDataFromRequest(request)
    message = Coder(inputText)
    jsonData = json.dumps({
        'outputText': message.decode(rotate),
        'frequencyDict': message.frequency_dict(),
        'unravelText': message.unravel_text()
    })
    return HttpResponse(jsonData, content_type='application/json')


# it is not a view, just helping func
def getCaesarDataFromRequest(request):
    """ collects specified data from json-request.
    :returns inputText, rotate """
    jsonData = request.GET['jsonData']
    data = json.loads(jsonData)
    return data['inputText'], int(data['rotate'])