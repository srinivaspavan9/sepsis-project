from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('formhandle/',views.formhandle,name="form-handle"),
    path('graphs/',views.graphs,name="graphs"),
]
