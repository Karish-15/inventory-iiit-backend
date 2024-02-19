from django.urls import path

from . import views

urlpatterns = [
    path('list/sw', views.SW_ResourcesListAPIView.as_view(), name='sw_resources_list'),
    path('create/sw', views.SW_ResourcesCreateAPIView.as_view(), name='sw_resources_create'),
    path('update/sw/<int:product_id>', views.SW_ResourcesUpdateDestroyAPIView.as_view(), name='sw_resources_update'),
    path('sw/<int:product_id>', views.SW_ResourcesRetrieveAPIView.as_view(), name='sw_resources_detail'),
    path('list/computing', views.Computing_ResourcesListAPIView.as_view(), name='computing_resources_list'),
    path('create/computing', views.Computing_ResourcesCreateAPIView.as_view(), name='computing_resources_create'),
    path('update/computing/<int:product_id>', views.Computing_ResourcesUpdateDestroyAPIView.as_view(), name='computing_resources_update'),
    path('computing/<int:product_id>', views.Computing_ResourcesRetrieveAPIView.as_view(), name='computing_resources_detail'),
    path('list/io', views.IO_ResourcesListAPIView.as_view(), name='io_resources_list'),
    path('create/io', views.IO_ResourcesCreateAPIView.as_view(), name='io_resources_create'),
    path('update/io/<int:product_id>', views.IO_ResourcesUpdateDestroyAPIView.as_view(), name='io_resources_update'),
    path('io/<int:product_id>', views.IO_ResourcesRetrieveAPIView.as_view(), name='io_resources_detail'),
    path('list/nw', views.NW_ResourcesListAPIView.as_view(), name='nw_resources_list'),
    path('create/nw', views.NW_ResourcesCreateAPIView.as_view(), name='nw_resources_create'),
    path('update/nw/<int:product_id>', views.NW_ResourcesUpdateDestroyAPIView.as_view(), name='nw_resources_update'),
    path('nw/<int:product_id>', views.NW_ResourcesRetrieveAPIView.as_view(), name='nw_resources_detail'),
    path('search', views.ResourcesSearchAPIView.as_view(), name='resources_search'),
]