from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from django.utils import timezone
from datetime import datetime
from unittest.mock import Mock

from stream.models import Purr

class ModelTests(TestCase):

    def setUp(self):
        self.mocked_now = datetime(2019, 1, 2)
        timezone.now = Mock(return_value=self.mocked_now)
        self.purr = Purr(
            author='Author',
            content='Content',
        )

    def test_mock_datetime_now(self):
        self.assertEquals(timezone.now(), self.mocked_now)

    def test_purr_contains_all_attributes(self):
        self.purr.clean()
        self.purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, 'Author')
        self.assertEquals(actual.content, 'Content')

    def test_author_cannot_save_null(self):
        with self.assertRaisesMessage(IntegrityError, 'NOT NULL constraint failed: stream_purr.author'):
            self.purr.author = None
            self.purr.save()

    def test_author_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            self.purr.author = None
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be null.']})

    def test_author_blank_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            self.purr.author = ''
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['This field cannot be blank.']})

    def test_author_cannot_be_longer_than_32_chars(self):
        invalid_author = 33 * 'a'

        with self.assertRaises(ValidationError) as cm:
            self.purr.author = invalid_author
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'author': ['Ensure this value has at most 32 characters (it has 33).']})

    def test_author_is_allowed_to_be_32_chars(self):
        valid_author = 32 * 'a'
        self.purr.author=valid_author
        self.purr.full_clean()
        self.purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.author, valid_author)

    def test_content_cannot_save_null(self):
        with self.assertRaisesMessage(IntegrityError, 'NOT NULL constraint failed: stream_purr.content'):
            self.purr.content = None
            self.purr.save()

    def test_content_null_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            self.purr.content = None
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'content': ['This field cannot be null.']})

    def test_content_blank_is_invalid(self):
        with self.assertRaises(ValidationError) as cm:
            self.purr.content = ''
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'content': ['This field cannot be blank.']})

    def test_content_cannot_be_longer_than_141_chars(self):
        invalid_content = 142 * 'b'

        with self.assertRaises(ValidationError) as cm:
            self.purr.content = invalid_content
            self.purr.full_clean()

        self.assertEqual(cm.exception.message_dict, {'content': ['Ensure this value has at most 141 characters (it has 142).']})

    def test_content_is_allowed_to_be_141_chars(self):
        valid_content = 141 * 'a'
        self.purr.content = valid_content
        self.purr.full_clean()
        self.purr.save()

        actual = Purr.objects.first()
        self.assertEquals(actual.content, valid_content)
