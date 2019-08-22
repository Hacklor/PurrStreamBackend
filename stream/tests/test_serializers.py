from django.test import TestCase

from stream.models import Purr
from stream.serializers import PurrSerializer

class SerializerTests(TestCase):

    def test_experiment_creating_valid_purr_instance(self):
        purr_attributes = {
            'author': 'Author',
            'content': 'Content of a purr',
        }
        serializer = PurrSerializer(data=purr_attributes)
        self.assertTrue(serializer.is_valid())
        actual = serializer.save()

        self.assertEquals(actual.author, 'Author')
        self.assertEquals(actual.content, 'Content of a purr')

        purr = Purr.objects.first()
        self.assertEquals(purr.author, 'Author')
        self.assertEquals(purr.content, 'Content of a purr')
