from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateRoom, name='create_room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]