from .config import *
from unittest.mock import Mock, patch
from django.test import TestCase, Client, RequestFactory
from .. import views as view
from forwarder.models import Route


class GetSmsTest(TestCase):

    def test_does_nothing_if_not_my_number(self):
        response = view.getsms('fake', "I am yesoch yay")
        self.assertContains(response, view.FAIL_INVALID_NUMBER)

    def test_does_different_if_my_number(self):
        response = view.getsms(environ['MY_NUMBER'], "I am yesoch yay")
        self.assertNotContains(response, view.FAIL_INVALID_NUMBER)

class ProcessCommandTest(TestCase):

    def setUp(self):
        valid_route = {'key': "test", 'url': 'none', 
                'auth_username': 'a', 'auth_password': 'b'}
        self.route = Route.objects.create(**valid_route)

    def test_returns_no_route_fail(self):
        invalid_command = {"command": "bamf", "args": "23"}
        response = view.process_command(invalid_command)
        self.assertContains(response, view.FAIL_BAD_ROUTE)

    @patch('sms.views.forward')
    def test_returns_status_code(self, mock):
        mock.return_value = 300
        response = view.process_command({"command": "test", "args": 'none'})
        self.assertContains(response, 300)
        
