from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from stream.models import Purr

class ModelTests(TestCase):

    def test_purr_contains_author_and_content(self):
        purr = Purr(
            author='Author',
            content='Content',
        )
        purr.clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, 'Author')
        self.assertEquals(actual.content, 'Content')

    def test_author_cannot_save_null(self):
        with self.assertRaisesMessage(IntegrityError, 'NOT NULL constraint failed: stream_purr.author'):
            Purr().save()

    def test_author_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(
                content='Content',
            ).full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be null.']})

    def test_author_blank_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(
                author='',
                content='Content',
            ).full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be blank.']})

    def test_author_cannot_be_longer_than_32_chars(self):
        invalid_author = 33 * 'a'
        with self.assertRaises(ValidationError) as cm:
            Purr(
                author=invalid_author,
                content='Content',
            ).full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['Ensure this value has at most 32 characters (it has 33).']})

    def test_author_is_allowed_to_be_32_chars(self):
        valid_author = 32 * 'a'
        purr = Purr(
            author=valid_author,
            content='Content',
        )
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, valid_author)

    def test_content_cannot_save_null(self):
        with self.assertRaisesMessage(IntegrityError, 'NOT NULL constraint failed: stream_purr.content'):
            Purr(author='Author').save()

    def test_content_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(
                author='Author',
            ).full_clean()

        self.assertEqual(cm.exception.message_dict, {'content': ['This field cannot be null.']})
