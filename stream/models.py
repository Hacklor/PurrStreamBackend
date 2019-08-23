from django.db import models

from datetime import datetime

class Purr(models.Model):
    author = models.CharField(max_length=32, default=None)
    content = models.CharField(max_length=141, default=None)

    def datetime_now(self):
        return datetime.now()
