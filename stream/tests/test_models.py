from django.test import TestCase
from django.core.exceptions import ValidationError

from stream.models import Purr

class ModelTests(TestCase):

    def test_contains_author_and_content(self):
        purr = Purr(
            author='Author',
            content='Content of a purr'
        )
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.content, 'Content of a purr')
        self.assertEquals(actual.author, 'Author')

    def test_content_cannot_be_null(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='Author').full_clean()

        # Still looking for a cleaner, less brittle way to test this
        self.assertEqual(cm.exception.message_dict, {'content': ['This field cannot be null.']})

    def test_content_cannot_be_blank(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='Author', content='').full_clean()

        # Still looking for a cleaner, less brittle way to test this
        self.assertEqual(cm.exception.message_dict, {'content': ['This field cannot be blank.']})

    def test_content_allowed_141_chars(self):
        content = 141 * 'a'

        purr = Purr(
            author='Author',
            content=content,
        )
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.content, content)

    def test_content_allowed_special_characters(self):
        purr = Purr(
            author='Author',
            content='Content !@#$%,".',
        )
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.content, 'Content !@#$%,".')

    def test_content_not_allowed_142_chars(self):
        with self.assertRaises(ValidationError) as cm:
            content = 142 * 'b'
            Purr(
                author='Author',
                content=content
            ).full_clean()

        self.assertEqual(cm.exception.message_dict, {'content': ['Ensure this value has at most 141 characters (it has 142).']})

    def test_author_cannot_be_null(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(content='Content').full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be null.']})

    def test_author_cannot_be_blank(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='', content='Content').full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be blank.']})

    def test_author_can_contain_alphanumeric(self):
        purr = Purr(
            author='123abcxyzABCXYZ',
            content='Content of a purr'
        )
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, '123abcxyzABCXYZ')

    def test_author_cannot_contain_non_alphanumeric(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='author!', content='Content').full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['Only alphanumeric characters are allowed.']})
