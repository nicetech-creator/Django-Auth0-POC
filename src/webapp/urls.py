from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile),
    path('', include('django.contrib.auth.urls')),
]