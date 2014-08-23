#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Categories(models.Model):

    name  = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
