from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Coder


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def encode(request):
    input_text, rotate = get_caesar_data_from_request(request)
    message = Coder(input_text)
    json_data = json.dumps({
        'output_text': message.encode(rotate),
        'frequency_dict': message.frequency_dict(),
        'restored_text': message.restore_message()
    })
    return HttpResponse(json_data, content_type='application/json')


def decode(request):
    input_text, rotate = get_caesar_data_from_request(request)
    message = Coder(input_text)
    json_data = json.dumps({
        'output_text': message.encode(rotate),
        'frequency_dict': message.frequency_dict(),
        'restored_text': message.restore_message()
    })
    return HttpResponse(json_data, content_type='application/json')


def get_caesar_data_from_request(request):
    """ collects specified data from json-request.
    :returns inputText, rotate """
    json_data = request.GET['json_data']
    data = json.loads(json_data)
    return data['input_text'], int(data['rotate'])