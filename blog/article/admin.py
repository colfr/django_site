#-*- coding:utf-8 -*-
from django.contrib import admin
from article.models import Categorie, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Categorie)
admin.site.register(Article,ArticleAdmin)