from django.urls import path

from . import views

urlpatterns = [
    path('list', views.CompositeDevicesListAPIView.as_view()),
    path('create', views.CompositeDevicesCreateAPIView.as_view()),
    path('update/<int:id>', views.CompositeDevicesUpdateDestroyAPIView.as_view()),
    path('retrieve/<int:id>', views.CompositeDevicesRetrieveAPIView.as_view()),
]