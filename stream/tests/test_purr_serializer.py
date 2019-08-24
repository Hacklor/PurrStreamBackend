from django.test import TestCase
from rest_framework import serializers

from stream.serializers import PurrSerializer
from stream.models import Purr

class PurrSerializerTests(TestCase):

    def test_creates_valid_purr_instance(self):
        purr_attributes = {
            'author': 'Author',
            'content': 'Content of a purr',
        }
        serializer = PurrSerializer(data=purr_attributes)
        self.assertTrue(serializer.is_valid())
        actual = serializer.save()

        self.assertIsInstance(actual, Purr)
        self.assertEquals(actual.id, 1)
        self.assertEquals(actual.author, 'Author')
        self.assertEquals(actual.content, 'Content of a purr')

    def test_retrieves_valid_purr_instance(self):
        purr = Purr(
            author='Author',
            content='Content',
        )
        purr.save()

        purr_attributes = {
            'id': 1,
            'author': 'Author',
            'content': 'Content',
        }
        serializer = PurrSerializer(instance=purr)
        self.assertEquals(serializer.data, purr_attributes)
