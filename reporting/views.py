from rest_framework import generics, views 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins
from rest_framework.response import Response

from .models import Reports
from .serializers import ReportsSerializer

class ReportsSearchAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        filters = request.data.get('filters', None)
        if filters is None:
            return Response({'error': 'filters is required'}, status=400)

        results = Reports.objects.all().filter(**filters)
        serializer = ReportsSerializer(results, many=True)

        return Response(
        {
            "total": len(serializer.data),
            "data": serializer.data,
        }, 
        status=200
        )

class ReportsListAPIView(generics.ListCreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]

class ReportsCreateAPIView(generics.CreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = [IsAuthenticated,]

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
