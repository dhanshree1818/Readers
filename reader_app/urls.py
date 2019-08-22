from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from reader_app import views

urlpatterns = [
    path('',views.index, name="base"),
    path('register/',views.register,name="register"),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),

]
