from django.shortcuts import render

from sms.utils import parse_message, clean_number
from django.http import HttpResponse
from django_twilio.decorators import twilio_view
from django_twilio.client import twilio_client

#@twilio_view
def index(request):
    from_number = clean_number(request.POST.get('From', '0'))
    message = request.POST.get('Body', '')
    return getsms(from_number, message)

def getsms(from_number, message):
    if from_number == '12487943292':
        route = parse_message(message)
        route_function = ROUTES[route['route']]
        response = route_function(*route['args'])
    else:
        response = ROUTES['outside'](from_number, message)
    if isinstance(response, dict) or isinstance(response, str):
        return sendsms(response)
    return HttpResponse("Complete.")


def sendsms(messages):
    if isinstance(messages, str):
        messages = { MY_NUMBER: messages }
    return HttpResponse('Sent.')
