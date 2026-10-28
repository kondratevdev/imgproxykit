from django.urls import path

from test_apps.django.server import views

urlpatterns = [
    path('images/', views.django_images, name='images'),
    path('api/images/', views.drf_images, name='api_images'),  # ty: ignore[no-matching-overload]
]
