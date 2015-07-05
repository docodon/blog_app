from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs import views

urlpatterns = patterns('',
    url(r'^list/$',views.index,name='index'),
    url(r'^new_blog/$',views.add_blog,name='add_blog'),
)