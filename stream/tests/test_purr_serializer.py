from django.test import TestCase

from stream.serializers import PurrSerializer

class PurrSerializerTests(TestCase):

    def test_initialize(self):
        PurrSerializer()
