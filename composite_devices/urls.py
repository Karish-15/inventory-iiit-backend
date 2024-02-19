from django.urls import path

from . import views

urlpatterns = [
    path('list', views.CompositeDevicesListAPIView.as_view(), name='composite_devices_list'),
    path('create', views.CompositeDevicesCreateAPIView.as_view(), name='composite_devices_create'),
    path('update/<int:id>', views.CompositeDevicesUpdateDestroyAPIView.as_view(), name='composite_devices_update'),
    path('<int:id>', views.CompositeDevicesRetrieveAPIView.as_view(), name='composite_devices_detail'),
    path('search', views.CompositeDevicesSearchAPIView.as_view(), name='composite_devices_search'),
]