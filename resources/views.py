from rest_framework import generics, views 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins
from rest_framework.response import Response

from .models import SW_Resources, Computing_Resources, IO_Resources, NW_Resources
from .serializers import SW_ResourcesSerializer, Computing_ResourcesSerializer, IO_ResourcesSerializer, NW_ResourcesSerializer

from utils.searching import search_resource

"""
TO-DO:
    - Make Generic API for all resources
"""

class ResourcesSearchAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        filters = request.data.get('filters', None)
        if filters is None:
            return Response({'error': 'filters is required'}, status=400)

        response = search_resource(filters)

        return Response({
            response
        }, status=200)

class SW_ResourcesListAPIView(generics.ListAPIView):
    # queryset = SW_Resources.objects.all().filter()
    serializer_class = SW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return SW_Resources.objects.all().filter(self.request.user)

class SW_ResourcesCreateAPIView(generics.CreateAPIView):
    queryset = SW_Resources.objects.all()
    serializer_class = SW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

class SW_ResourcesUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = SW_Resources.objects.all()
    serializer_class = SW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'product_id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SW_ResourcesRetrieveAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        if product_id is None:
            return Response({'error': 'product_id is required'}, status=400)
        sw_resource = SW_Resources.objects.get(product_id=product_id)
        serializer  = SW_ResourcesSerializer(sw_resource)
        return Response(serializer.data, status=200)

class Computing_ResourcesListAPIView(generics.ListAPIView):
    # queryset = Computing_Resources.objects.all()
    serializer_class = Computing_ResourcesSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        return Computing_Resources.objects.all().filter(self.request.user)

class Computing_ResourcesCreateAPIView(generics.CreateAPIView):
    queryset = Computing_Resources.objects.all()
    serializer_class = Computing_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

class Computing_ResourcesUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Computing_Resources.objects.all()
    serializer_class = Computing_ResourcesSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'product_id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Computing_ResourcesRetrieveAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        if product_id is None:
            return Response({'error': 'product_id is required'}, status=400)
        computing_resource = Computing_Resources.objects.get(product_id=product_id)
        serializer = Computing_ResourcesSerializer(computing_resource)
        return Response(serializer.data, status=200)

class IO_ResourcesListAPIView(generics.ListAPIView):
    # queryset = IO_Resources.objects.all()
    serializer_class = IO_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return IO_Resources.objects.all().filter(self.request.user)

class IO_ResourcesCreateAPIView(generics.CreateAPIView):
    queryset = IO_Resources.objects.all()
    serializer_class = IO_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

class IO_ResourcesUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = IO_Resources.objects.all()
    serializer_class = IO_ResourcesSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'product_id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class IO_ResourcesRetrieveAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        if product_id is None:
            return Response({'error': 'product_id is required'}, status=400)
        io_resource = IO_Resources.objects.get(product_id=product_id)
        serializer = IO_ResourcesSerializer(io_resource)
        return Response(serializer.data, status=200)

class NW_ResourcesListAPIView(generics.ListAPIView):
    # queryset = NW_Resources.objects.all()
    serializer_class = NW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return NW_Resources.objects.all().filter(self.request.user)

class NW_ResourcesCreateAPIView(generics.CreateAPIView):
    queryset = NW_Resources.objects.all()
    serializer_class = NW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]

class NW_ResourcesUpdateDestroyAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = NW_Resources.objects.all()
    serializer_class = NW_ResourcesSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'product_id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class NW_ResourcesRetrieveAPIView(views.APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        if product_id is None:
            return Response({'error': 'product_id is required'}, status=400)
        nw_resource = NW_Resources.objects.get(product_id=product_id)
        serializer = NW_ResourcesSerializer(nw_resource)
        return Response(serializer.data, status=200)


