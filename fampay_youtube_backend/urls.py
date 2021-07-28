from django.urls import path

from . import views

urlpatterns = [
    path('add_key', views.AddAPIKey.as_view()),
]
