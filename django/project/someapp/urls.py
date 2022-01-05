from django.urls import path

from .views import index, a_index

urlpatterns = [
    path('', index),
    path('/', index),
    path('async', a_index),
]
