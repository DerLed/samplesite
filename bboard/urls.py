from django.urls import path

from .views import index, index1
urlpatterns = [
    path('', index),
    path('1', index1),
]
