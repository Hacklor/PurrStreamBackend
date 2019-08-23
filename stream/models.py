from django.db import models

class Purr(models.Model):
    author = models.CharField(max_length=25, default=None)
