from rest_framework.test import APITestCase
from rest_framework import status

from django.utils import timezone
from unittest.mock import Mock

from stream.models import User, Purr

class ListPurrsApiTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Test',
            password='Pass',
            email='user@example.com',
            first_name='Test',
            last_name='User'
        )

        self.mocked_now = timezone.now()
        timezone.now = Mock(return_value=self.mocked_now)
        self.formatted_now = self.mocked_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_returns_success(self):
        response = self.client.get('/purrs/')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals('application/json', response['Content-Type'])

    def test_returns_purr_as_json(self):
        Purr.objects.create(user=self.user, content='Content')

        response = self.client.get('/purrs/')

        expected = '[{"id":1,"user":{"id":1,"username":"Test"},"content":"Content","created_at":"' + self.formatted_now + '"}]'
        self.assertEquals(expected, response.content.decode("utf-8"))

    def test_returns_empty_list_of_purrs(self):
        response = self.client.get('/purrs/')

        self.assertEquals([], response.data)

    def test_returns_list_of_multiple_purrs(self):
        purr0 = Purr.objects.create(user=self.user, content='Content1')
        purr1 = Purr.objects.create(user=self.user, content='Content2')
        purr2 = Purr.objects.create(user=self.user, content='Content3')

        self.assertEquals(purr0.created_at, purr1.created_at)

        response = self.client.get('/purrs/')

        self.assertEquals(purr0.id, response.data[0]['id'])
        self.assertEquals(purr0.user.id, response.data[0]['user']['id'])
        self.assertEquals(purr0.user.username, response.data[0]['user']['username'])
        self.assertEquals(purr0.content, response.data[0]['content'])

        self.assertEquals(purr1.id, response.data[1]['id'])
        self.assertEquals(purr1.user.id, response.data[1]['user']['id'])
        self.assertEquals(purr1.user.username, response.data[1]['user']['username'])
        self.assertEquals(purr1.content, response.data[1]['content'])

        self.assertEquals(purr2.id, response.data[2]['id'])
        self.assertEquals(purr2.user.id, response.data[2]['user']['id'])
        self.assertEquals(purr2.user.username, response.data[2]['user']['username'])
        self.assertEquals(purr2.content, response.data[2]['content'])

class CreatePurrApiTests(APITestCase):

    def setUp(self):
        response = self.client.post('/accounts/register/', {
            'username':'Test',
            'password':'Welcome123!',
            'password_confirm':'Welcome123!',
            'email':'user@example.com',
            'first_name':'Test',
            'last_name':'User',
        })
        response = self.client.post('/accounts/login/', {'login':'Test', 'password':'Welcome123!'})

        self.mocked_now = timezone.now()
        timezone.now = Mock(return_value=self.mocked_now)
        self.formatted_now = self.mocked_now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_returns_status_created(self):
        purr = {'content': 'Content1'}
        response = self.client.post('/purrs/', purr)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)

    def test_can_list_created_purr(self):
        purr = {'content': 'Content1'}
        self.client.post('/purrs/', purr)

        response = self.client.get('/purrs/')

        self.assertEquals(1, response.data[0]['id'])
        self.assertEquals(1, response.data[0]['user']['id'])
        self.assertEquals('Test', response.data[0]['user']['username'])
        self.assertEquals('Content1', response.data[0]['content'])
        self.assertEquals(self.formatted_now, response.data[0]['created_at'])

    def test_returns_bad_request_invalid_purr(self):
        purr = {'content': ''}
        response = self.client.post('/purrs/', purr)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('blank', response.data['content'][0].code)

class DestroyPurrApiTests(APITestCase):

    def setUp(self):
        response = self.client.post('/accounts/register/', {
            'username':'Test',
            'password':'Welcome123!',
            'password_confirm':'Welcome123!',
            'email':'user@example.com',
            'first_name':'Test',
            'last_name':'User',
        })
        response = self.client.post('/accounts/login/', {'login':'Test', 'password':'Welcome123!'})

    def test_destroy_existing_purr(self):
        self.client.post('/purrs/', {'content': 'Content1'})

        response = self.client.delete('/purrs/1/')
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

        self.assertEquals([], self.client.get('/purrs/').data)

    # I do not agree with this behavior
    # You got what you wished for, mission accomplished
    # Returning a 204 is fine! On the outside it doesn't matter
    # But leaving it for now, maybe I'll override later
    def test_destroy_non_existing_purr(self):
        response = self.client.delete('/purrs/1/')
        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)

