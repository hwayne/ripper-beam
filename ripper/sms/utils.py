import shlex
from re import sub

def clean_number(number):
    return sub("\D", "", number)


def parse_message(message):
    """Breaks an input message (sms, email, etc) into a dict of form
               {'command': first_token, 'args': [array_of_rest_of_tokens]}"""
    message = "Empty Message" if not message else message
    token_list = shlex.split(message)
    command = token_list.pop(0).lower()
    return {'command': command, 'args': token_list}
