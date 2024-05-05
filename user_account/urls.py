from django.urls import path
from . import views

urlpatterns = [
    path('giveuser', views.giveUserFromTokenAPIView.as_view()),
    path('register', views.registerUserAPIView.as_view(), name='register-user'),
    path('get-user-list', views.getUserList.as_view(), name='get-user-list'),
    path('is-admin-check', views.isAdminCheck.as_view(), name='is-admin-check'),
]
