from django.test import TestCase

from stream.models import Purr

class ModelTests(TestCase):

    def test_contains_author(self):
        purr = Purr(
            author='Author',
        )
        purr.clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, 'Author')
