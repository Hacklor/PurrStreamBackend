from django.test import TestCase

from stream.models import Purr

class ModelTests(TestCase):

    def create_instance(self):
        Purr()
