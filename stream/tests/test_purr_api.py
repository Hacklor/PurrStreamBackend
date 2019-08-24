from django.test import TestCase

from rest_framework.test import APIRequestFactory

class PurrApiTests(TestCase):

    def test_can_request_list_of_purrs(self):
        response = self.client.get('/purrs/', format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'test response')
