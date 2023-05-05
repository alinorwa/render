from django.urls import path
from .views import *



urlpatterns = [
    path('' , home , name='home' ),
    path('admin/', admin, name='admin'),
    path('about/' , about , name='about')
]