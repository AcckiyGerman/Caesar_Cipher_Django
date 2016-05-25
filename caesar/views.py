import json
from django.shortcuts import render
from django.http import HttpResponse
from caesar.utils import get_caesar_data_from_request, Coder


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def encode(request):
    input_text, rotate = get_caesar_data_from_request(request)
    message = Coder(input_text)
    restored_message = message.restore_message()
    json_data = json.dumps({
        'output_text': message.encode(rotate),
        'frequency_dict': message.frequency_dict(),
        'restored_text': restored_message[0],
        'probably_rotate': restored_message[1]
    })
    return HttpResponse(json_data, content_type='application/json')


def decode(request):
    input_text, rotate = get_caesar_data_from_request(request)
    message = Coder(input_text)
    restored_message = message.restore_message()
    json_data = json.dumps({
        'output_text': message.encode(rotate),
        'frequency_dict': message.frequency_dict(),
        'restored_text': restored_message[0],
        'probably_rotate': restored_message[1]
    })
    return HttpResponse(json_data, content_type='application/json')


