# progress/models.py
from django.db import models
from django.contrib.auth.models import User

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    progress_percent = models.IntegerField(default=0)
