from django.test import TestCase
from ..forward import forward, post, ObjectDoesNotExist
from ..models import Route
from unittest.mock import patch

class forwardTestCase(TestCase):

    def test_contracts_works(self):
        with self.assertRaises(Exception):
            forward(2, [0])

    def test_raises_if_model_not_exist(self):
        with self.assertRaises(ObjectDoesNotExist):
            forward("blue")

    @patch('forwarder.forward.post')
    def test_gets_model_with_same_key(self, _):
        Route.objects.create(key="blue", url="25")
        forward("blue")

    @patch('forwarder.forward.post')
    def test_sends_request_with_model(self, mock):
        route = Route.objects.create(key="blue", url="25")
        forward("blue")
        mock.assert_called_with(route)

    @patch('forwarder.forward.post')
    def test_sends_request_with_called_params(self, mock):
        route = Route.objects.create(key="blue", url="25")
        forward("blue", [1,2,3])
        mock.assert_called_with(route, [1,2,3])
