from django.db import models

# Create your models here.
#pronado git
class spam_ham(models.Model):
    text=models.CharField(max_length=10000)
    result=models.CharField(max_length=4)