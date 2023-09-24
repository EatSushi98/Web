from django.contrib import admin
from django.urls import path
from HOME import views


urlpatterns = [
    path("", views.index, name="home"),
    path("About", views.about , name="About"),
    path("Contact", views.contact , name="Contact"),
]

