from django_twilio.decorators import twilio_view
from .utils import parse_message, clean_number
from forwarder.forward import forward
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from os import environ

xml = lambda x: "<Response><Message>{}</Message></Response>".format(x)
FAIL_INVALID_NUMBER = xml("This is not an authorized number.") # Twilio weirdness
FAIL_BAD_ROUTE = xml("No matching route found.") # Twilio weirdness

@twilio_view
def index(request):
    from_number = clean_number(request.POST.get('From', '0'))
    message = request.POST.get('Body', '')
    return getsms(from_number, message)

def getsms(from_number, message):
    if from_number == environ['MY_NUMBER']:
        command = parse_message(message)
        return process_command(command)
    else:
        return HttpResponse(FAIL_INVALID_NUMBER, content_type = 'text/xml')

def process_command(command):
    try:
        status = forward(command['command'], *command['args'])
        response = xml("Command returned {}.".format(status))
    except ObjectDoesNotExist:
        response = FAIL_BAD_ROUTE
    return HttpResponse(response, content_type = 'text/xml')
