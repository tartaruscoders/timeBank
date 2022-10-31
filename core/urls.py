from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.loader, name="loader"),
    path('home/', views.home, name="home"),

]