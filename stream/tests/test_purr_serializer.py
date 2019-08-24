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

    def test_validates_valid_purr(self):
        serializer = PurrSerializer(data=self.purr_attributes)
        self.assertTrue(serializer.is_valid())

    def test_validates_invalid_purr(self):
        self.purr_attributes['author'] = ''

        serializer = PurrSerializer(data=self.purr_attributes)
        self.assertFalse(serializer.is_valid())

    def test_creating_valid_purr(self):
        serializer = PurrSerializer(instance=self.purr)
        serializer.create(self.purr_attributes)

        actual = Purr.objects.first()
        self.assertIsInstance(actual, Purr)
        self.assertEquals(actual.id, 1)
        self.assertEquals(actual.author, self.purr_attributes['author'])
        self.assertEquals(actual.content, self.purr_attributes['content'])

    def test_serializes_valid_purr(self):
        self.purr.save()

        serializer = PurrSerializer(instance=self.purr)

        self.assertEquals(serializer.data['id'], 1)
        self.assertEquals(serializer.data['author'], self.purr_attributes['author'])
        self.assertEquals(serializer.data['content'], self.purr_attributes['content'])
