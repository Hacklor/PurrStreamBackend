from django.test import TestCase
from rest_framework import serializers

from stream.serializers import PurrSerializer

class PurrSerializerTests(TestCase):

    def test_initialize(self):
        self.assertIsInstance(PurrSerializer(), serializers.ModelSerializer)
