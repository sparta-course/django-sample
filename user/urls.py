from django.contrib import admin
from django.urls import path, include

from user import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    
    path('cart/', views.UserCartView.as_view()),
]
