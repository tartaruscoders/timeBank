from django.urls import path
from . import views
urlpatterns = [
    path('', views.loader, name="loader"),
    path('home/', views.home, name="home")
]