from django.urls import path
from . import views

urlpatterns = [
    path('', views.nearby, name='nearby'),
]