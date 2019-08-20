from django.test import TestCase
from django.db.utils import IntegrityError

from stream.models import Purr

class ModelTests(TestCase):

    def test_contains_author_and_content(self):
        Purr.objects.create(
            author='Author of the purr',
            content='Content of a purr'
        )

        purr = Purr.objects.first()
        self.assertEquals(purr.content, 'Content of a purr')
        self.assertEquals(purr.author, 'Author of the purr')

    def test_content_cannot_be_null(self):
        # I would like to test the message as well
        # so that I know it fails for the correct reason
        # How?
        with self.assertRaises(IntegrityError):
            Purr.objects.create(author='Author of the purr')


    def test_content_cannot_be_blank(self):
        with self.assertRaises(IntegrityError):
            Purr.objects.create(
                author='Author of the purr',
                content='',
            )

    # content cannot be blank
    # content is allowed to be 141 characters
    # content is not allowed to be 142 characters
    # content is allowed special characters
    # author cannot be null
    # author cannot be blank
    # author may contain alphanumeric characters
    # author may not contain non alphanumeric characters
