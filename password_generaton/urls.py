from django.urls import path
from ganerator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('description', views.description, name='description')
]
