import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from caesar.models import Message


def index(request):
    context = {}
    return render(request, 'caesar/index.html', context)


def handler(request):
    # get data
    json_data = request.GET['json_data']
    data = json.loads(json_data)
    input_text = data['input_text'].lower()
    rotate = int(data['rotate'])
    # work with data
    message = Message(text=input_text, rotate=rotate, date=timezone.now())
    if '/encode/' in request.path:
        output_text = message.encode(rotate)
    elif '/decode/' in request.path:
        output_text = message.decode(rotate)
    frequency_dict = message.frequency_dict()
    restored_message, probably_rotate = message.restore_message()
    message.save()
    # send data back to user
    json_data = json.dumps({
        'output_text': output_text,
        'frequency_dict': frequency_dict,
        'restored_text': restored_message,
        'probably_rotate': probably_rotate
    })
    return HttpResponse(json_data, content_type='application/json')


class HistoryView(generic.ListView):
    template_name = 'caesar/history.html'
    context_object_name = 'messages_list'

    def get_queryset(self):
        quantity = Message.objects.count()
        return Message.objects.order_by('date')[quantity-5:]