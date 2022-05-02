from django.contrib import admin
from django.urls import path
from home.views import about
from home.views import home,about
urlpatterns = [
    path("",home,name="Wel-come"),
    path("about", about, name="Wel-about"),

]