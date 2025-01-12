from django.contrib import admin
from django.urls import path, include
from services import views

urlpatterns = [
    path("diet", views.diet, name="diet"),
    path("exercise", views.exercise, name="exercise"),
    path("planning", views.planning, name="planning"),
]