from django.contrib import admin
from django.urls import path
from home.views import about
from store.views import store_home

urlpatterns = [
    path("",store_home,name="ecom-store-home"),
    path("<slug:category_slug>/", store_home, name="ecom-store-category"),


]