from email.policy import default
from secrets import choice
from tkinter import CASCADE
from django.db import models

from authentication.models import User

# Create your models here.
class Task(models.Model):
    STATE_OPTION =[
        ('D','DONE'),
        ('P','IN_PROGRESS'),
        ('N', 'TO_DO')
    ]
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    state = models.CharField(choices = STATE_OPTION, max_length = 30, default = 'N')
    description = models.CharField(max_length = 512, null = False, blank = False)

    def __str__(self):
        return f' {self.pk} {self.owner}' 