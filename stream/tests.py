from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

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

    def test_author_cannot_save_null(self):
        with self.assertRaisesMessage(IntegrityError, 'NOT NULL constraint failed: stream_purr.author'):
            Purr().save()

    def test_author_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr().full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be null.']})

    def test_author_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr().full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be null.']})

    def test_author_blank_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='').full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be blank.']})

    def test_author_cannot_be_longer_than_32_chars(self):
        invalid_author = 33 * 'a'
        with self.assertRaises(ValidationError) as cm:
            Purr(author=invalid_author).full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['Ensure this value has at most 32 characters (it has 33).']})

    def test_author_is_allowed_to_be_32_chars(self):
        valid_author = 32 * 'a'
        purr = Purr(author=valid_author)
        purr.full_clean()
        purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, valid_author)
