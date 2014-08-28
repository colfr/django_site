#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url



urlpatterns = patterns('article.views',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'articles', name="articles"),
)
