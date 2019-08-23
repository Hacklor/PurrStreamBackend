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

    def test_author_blank_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            Purr(author='').full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be blank.']})
