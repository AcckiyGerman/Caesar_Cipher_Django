import json
from django.shortcuts import render
from django.http import HttpResponse
from caesar.utils import Coder


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def handler(request):
    # get data
    json_data = request.GET['json_data']
    data = json.loads(json_data)
    input_text = data['input_text']
    rotate = int(data['rotate'])
    # work with data
    message = Coder(input_text)
    if '/encode/' in request.path:
        output_text = message.encode(rotate)
    elif '/decode/' in request.path:
        output_text = message.decode(rotate)
    frequency_dict = message.frequency_dict()
    restored_message, probably_rotate = message.restore_message()
    # send data back to user
    json_data = json.dumps({
        'output_text': output_text,
        'frequency_dict': frequency_dict,
        'restored_text': restored_message,
        'probably_rotate': probably_rotate
    })
    return HttpResponse(json_data, content_type='application/json')