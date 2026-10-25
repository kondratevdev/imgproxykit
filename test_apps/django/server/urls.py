from django.urls import path

from test_apps.django.server import views

urlpatterns = [path('', views.images, name='images')]
