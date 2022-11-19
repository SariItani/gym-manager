from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomView.as_view()),
    path('home/', views.RoomView.as_view()),
]
