from django.db import models
from accounts.models import Account

class Task(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    is_completed = models.BooleanField(default=False)
