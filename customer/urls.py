""" Urls for the Customer app """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
]
