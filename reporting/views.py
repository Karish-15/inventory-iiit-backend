from django.db.models import Q
from rest_framework import generics, views 
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.response import Response
from datetime import datetime

from .models import Reports, UnderRepair
from .serializers import ReportsSerializer

class ReportsSearchAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, *args, **kwargs):
        filters = request.data.get('filters', None)
        if filters is None:
            return Response({'error': 'filters is required'}, status=400)
        
        fields = ["serial_number", "report_id", "stage"]
        Qr = None
        for field in fields:
            if field in filters:
                q = Q(**{"%s__contains" % field: filters.get(field, "") })
                Qr = Qr | q if Qr else q

        results = Reports.objects.all().filter(Qr)
        serializer = ReportsSerializer(results, many=True)

        return Response(
            {
                "total": len(serializer.data),
                "data": serializer.data,
            }, 
            status=200
        )

class ReportsListAPIView(generics.ListAPIView):
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]
    queryset = Reports.objects.all().order_by('-created_at')

class ReportsCreateAPIView(generics.CreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ReportsUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReportsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'report_id'

class checkReportExists(views.APIView):
    def post(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number', None)
        if serial_number is None:
            return Response({'error': 'serial_number is required'}, status=400)
        try:
            report = Reports.objects.get(serial_number=serial_number)
            if report.stage < 4:
                return Response({'status': True, 'report_id': report.report_id}, status=200)
        except Reports.DoesNotExist:
            pass
        return Response({'status': False}, status=200)
    
class updateReportingStage(views.APIView):
    def post(self, request, *args, **kwargs):
        report_id = request.data.get('report_id', None)
        stage = request.data.get('stage', None)
        if report_id is None or stage is None:
            return Response({'error': 'report_id and stage are required'}, status=400)
        try:
            report = Reports.objects.get(report_id=report_id)
            report.stage = stage
            
            if stage == '4':
                under_repair_report = UnderRepair.objects.get(report_id=report_id)
                under_repair_report.under_repair = False
                # set current date
                under_repair_report.expected_return_date = datetime.now()
                under_repair_report.save()
            elif stage == '3':
                under_repair_report = UnderRepair(
                    report_id=Reports.objects.get(report_id=report_id),
                    expected_return_date=datetime.strptime(request.data.get('expected_return_date', None), "%d-%m-%Y"),
                    repairing_company=request.data.get('repairing_company', None),
                    under_repair = True,
                )
                under_repair_report.save()
            report.save()
            return Response({'status': True}, status=200)
        except Reports.DoesNotExist:
            pass
        return Response({'status': False, 'message': "Report Does not exist"}, status=400)
