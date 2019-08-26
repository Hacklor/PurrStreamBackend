from rest_framework.test import APITestCase
from rest_framework import status

from stream.models import Purr

class PurrApiTests(APITestCase):

    def test_returns_success(self):
        response = self.client.get('/purrs/')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals('application/json', response['Content-Type'])

    def test_returns_empty_list_of_purrs(self):
        response = self.client.get('/purrs/')

        self.assertEquals([], response.data)

    def test_returns_purr_when_present(self):
        Purr.objects.create(author='Author', content='Content')

        response = self.client.get('/purrs/')

        expected = [ {'id': 1, 'author': 'Author', 'content': 'Content'} ]
        self.assertEquals(expected, response.data)
