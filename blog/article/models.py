#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Categorie(models.Model):

    name  = models.CharField(max_length=128, unique=True, verbose_name="Categorie")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Categorie)
    title    = models.CharField(max_length=128, verbose_name='Titre', null=False)
    date     = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    views    = models.IntegerField(default=0, editable=False)
    likes    = models.IntegerField(default=0, editable=False)
    slug     = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return u'%s' %self.title