from django.db import models
from django.core.validators import RegexValidator

class Purr(models.Model):
    alphanumeric_validator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    author = models.CharField(max_length=32, blank=False, null=False, default=None, validators=[alphanumeric_validator])
    content = models.CharField(max_length=141, blank=False, null=False, default=None)
