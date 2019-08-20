from django.test import TestCase

from stream.models import Purr

class ModelTests(TestCase):

    def test_purr_must_contain_author_and_content(self):
        Purr.objects.create(
            author='Author of the purr',
            content='Content of a purr'
        )

        purr = Purr.objects.first()
        self.assertEquals(purr.content, 'Content of a purr')
        self.assertEquals(purr.author, 'Author of the purr')

    # content cannot be null
    # content cannot be blank
    # content is allowed to be 141 characters
    # content is not allowed to be 142 characters
    # content is allowed special characters
    # author cannot be null
    # author cannot be blank
    # author may contain alphanumeric characters
    # author may not contain non alphanumeric characters
