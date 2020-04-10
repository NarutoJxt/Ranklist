from django.db import models

# Create your models here.

class User(models.Model):
    client = models.IntegerField(verbose_name="客户端id")
    score = models.IntegerField(verbose_name="分数")
