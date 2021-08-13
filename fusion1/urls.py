from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('showall',views.showallsub_data)
]