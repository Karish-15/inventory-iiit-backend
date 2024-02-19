from rest_framework import generics, views 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins
from rest_framework.response import Response

from .models import CompositeDevices
from .serializers import CompositeDevicesSerializer

class CompositeDevicesListAPIView(generics.ListCreateAPIView):
    queryset = CompositeDevices.objects.all()
    serializer_class = CompositeDevicesSerializer
    permission_classes = [IsAuthenticated,]

class CompositeDevicesCreateAPIView(generics.CreateAPIView):
    queryset = CompositeDevices.objects.all()
    serializer_class = CompositeDevicesSerializer
    permission_classes = [IsAuthenticated,]

class CompositeDevicesUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = CompositeDevices.objects.all()
    serializer_class = CompositeDevicesSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CompositeDevicesRetrieveAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if id is None:
            return Response({'error': 'id is required'}, status=400)
        composite_device = CompositeDevices.objects.get(id=id)
        serializer = CompositeDevicesSerializer(composite_device)
        return Response(serializer.data, status=200)

class CompositeDevicesSearchAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        filters = request.data.get('filters', None)
        if filters is None:
            return Response({'error': 'filters is required'}, status=400)
        composite_device = CompositeDevices.objects.all().filter(**filters)
        serializer = CompositeDevicesSerializer(composite_device, many=True)

        return Response({"total": len(serializer.data), "data": serializer.data}, status=200)
