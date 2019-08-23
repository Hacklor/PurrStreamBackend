from django.db import models

class Purr(models.Model):
    author = models.CharField(max_length=32, default=None)
    content = models.CharField(max_length=255, default=None)
