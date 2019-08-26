from rest_framework.test import APITestCase
from rest_framework import status

from stream.models import Purr

class ListPurrsApiTests(APITestCase):

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

class CreatePurrApiTests(APITestCase):

    def test_returns_status_created(self):
        purr = {'author': 'Author1', 'content': 'Content1'}
        response = self.client.post('/purrs/', purr)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)

    def test_can_list_created_purr(self):
        purr = {'author': 'Author1', 'content': 'Content1'}
        response = self.client.post('/purrs/', purr)

        response = self.client.get('/purrs/')
        expected = [
            {'id': 1, 'author': 'Author1', 'content': 'Content1'},
        ]
        self.assertEquals(expected, response.data)

    def test_returns_bad_request_invalid_purr(self):
        purr = {'author': '', 'content': 'Content1'}
        response = self.client.post('/purrs/', purr)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('blank', response.data['author'][0].code)
