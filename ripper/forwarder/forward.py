from django.core.exceptions import ObjectDoesNotExist
from .models import Route
from contracts import contract
from requests import post as requests_post
from requests.auth import HTTPDigestAuth

@contract
def forward(key: str, *args, **kwargs):
    return(post(Route.objects.get(key=key), *args, **kwargs))

def post(model, *args, **kwargs):
    url = model.url
    auth = HTTPDigestAuth(model.auth_username, model.auth_password)
    payload = {'args': args}
    response = requests_post(url, data=payload, auth=auth)
    return response.status_code
