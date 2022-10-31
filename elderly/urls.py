from django.urls import path
from . import views

app_name = "elderly"

urlpatterns = [
    path('login/', views.elderaccount, name="elderAccountLogin")
]