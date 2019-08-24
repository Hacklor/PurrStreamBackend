from django.test import TestCase
from rest_framework import serializers

from stream.serializers import PurrSerializer
from stream.models import Purr

class PurrSerializerTests(TestCase):

    def setUp(self):
        self.purr_attributes = {
            'author': 'Author',
            'content': 'Content of a purr',
        }
        self.purr = Purr(
            author='Author',
            content='Content of a purr',
        )

    def test_creates_valid_purr_instance(self):
        serializer = PurrSerializer(data=self.purr_attributes)
        self.assertTrue(serializer.is_valid())
        actual = serializer.save()

        self.assertIsInstance(actual, Purr)
        self.assertEquals(actual.id, 1)
        self.assertEquals(actual.author, self.purr_attributes['author'])
        self.assertEquals(actual.content, self.purr_attributes['content'])

    def test_retrieves_valid_purr_instance(self):
        self.purr.save()

        serializer = PurrSerializer(instance=self.purr)

        self.purr_attributes['id'] = 1
        self.assertEquals(serializer.data['id'], self.purr_attributes['id'])
        self.assertEquals(serializer.data['author'], self.purr_attributes['author'])
        self.assertEquals(serializer.data['content'], self.purr_attributes['content'])
