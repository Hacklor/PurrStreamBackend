from django.db import models

class Purr(models.Model):
    author = models.CharField(max_length=255, default=None)
