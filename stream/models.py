from django.db import models

from django.utils import timezone

class Purr(models.Model):
    author = models.CharField(max_length=32, default=None)
    content = models.CharField(max_length=141, default=None)
