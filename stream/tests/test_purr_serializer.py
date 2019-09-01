from django.test import TestCase
from rest_framework import serializers

from django.utils import timezone
from unittest.mock import Mock

from stream.serializers import PurrSerializer
from stream.models import User, Purr

class PurrSerializerTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='Test',
            password='Pass',
            email='user@example.com',
            first_name='Test',
            last_name='User'
        )
        self.purr_attributes = {
            'user_id': self.user.id,
            'content': 'Content of a purr',
        }
        self.purr = Purr(
            user_id=self.user.id,
            content='Content of a purr',
        )

        self.mocked_now = timezone.now()
        timezone.now = Mock(return_value=self.mocked_now)

    def test_validates_valid_purr(self):
        serializer = PurrSerializer(data=self.purr_attributes)
        self.assertTrue(serializer.is_valid())

    def test_validates_invalid_purr(self):
        self.purr_attributes['content'] = None

        serializer = PurrSerializer(data=self.purr_attributes)
        self.assertFalse(serializer.is_valid())

    def test_creating_valid_purr(self):
        serializer = PurrSerializer(instance=self.purr)
        serializer.create(self.purr_attributes)

        actual = Purr.objects.first()
        self.assertIsInstance(actual, Purr)
        self.assertEquals(actual.id, 1)
        self.assertEquals(actual.user_id, self.purr_attributes['user_id'])
        self.assertEquals(actual.content, self.purr_attributes['content'])
        self.assertEquals(actual.created_at, self.mocked_now)

    def test_serializes_valid_purr(self):
        self.purr.save()

        serializer = PurrSerializer(instance=self.purr)

        self.assertEquals(serializer.data['id'], 1)
        self.assertEquals(serializer.data['user']['id'], self.user.id)
        self.assertEquals(serializer.data['user']['username'], self.user.username)
        self.assertEquals(serializer.data['content'], self.purr_attributes['content'])
        self.assertIsNotNone(serializer.data['created_at'])
