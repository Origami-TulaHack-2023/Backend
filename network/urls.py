from django.urls import path
from .views import my_view


urlpatterns = [
    path('my_view/', my_view, name='my_view'),
]
