from rest_framework.test import APITestCase
from rest_framework import status

from stream.models import Purr

class PurrApiTests(APITestCase):

    def test_returns_success(self):
        response = self.client.get('/purrs/')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals('application/json', response['Content-Type'])

    def test_returns_purr_as_json(self):
        Purr.objects.create(author='Author', content='Content')

        response = self.client.get('/purrs/')

        expected = b'[{"id":1,"author":"Author","content":"Content"}]'
        self.assertEquals(expected, response.content)

    def test_returns_empty_list_of_purrs(self):
        response = self.client.get('/purrs/')

        self.assertEquals([], response.data)

    def test_returns_list_of_multiple_purrs(self):
        Purr.objects.create(author='Author1', content='Content1')
        Purr.objects.create(author='Author2', content='Content2')
        Purr.objects.create(author='Author3', content='Content3')

        response = self.client.get('/purrs/')

        expected = [
            {'id': 1, 'author': 'Author1', 'content': 'Content1'},
            {'id': 2, 'author': 'Author2', 'content': 'Content2'},
            {'id': 3, 'author': 'Author3', 'content': 'Content3'},
        ]
        self.assertEquals(expected, response.data)
