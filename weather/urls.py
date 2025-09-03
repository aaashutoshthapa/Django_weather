from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root URL of your app
]
