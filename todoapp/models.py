from django.db import models
from django.utils import timezone
# Create your models here.
class Data(models.Model):
    text=models.CharField(max_length=100,blank=False,unique=True)
    date = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f'{self.text[:12]}'

