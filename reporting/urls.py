from django.urls import path

from . import views

urlpatterns = [
    path('list', views.ReportsListAPIView.as_view(), name='reports_list'),
    path('create', views.ReportsCreateAPIView.as_view(), name='reports_create'),
    path('update/<uuid:report_id>', views.ReportsUpdateDestroyAPIView.as_view(), name='reports_update'),
    path('<uuid:report_id>', views.ReportsRetrieveAPIView.as_view(), name='reports_detail'),
    path('search', views.ReportsSearchAPIView.as_view(), name='reports_search'),
    path('check-if-report-exists', views.checkReportExists.as_view(), name='check_report_exists'),
    path('update-reporting-stage', views.updateReportingStage.as_view(), name='update_reporting_stage'),
]