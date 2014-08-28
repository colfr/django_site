#-*- coding:utf-8 -*-
from django.shortcuts import render
from article.models import Article
# Create your views here.


def articles(request):

    content_Article = Article.objects.all()


    return render(request,"article/articles.html",{'articles':content_Article})