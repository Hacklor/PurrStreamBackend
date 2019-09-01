from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Purr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False, blank=False)
    content = models.CharField(max_length=141, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
