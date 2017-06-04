# -*- coding: utf-8 -*-  
_author_ = 'clevertang'
from django.conf.urls import url

from .import views
urlpatterns = [
    url(r'^$',views.get_blogs),
]
