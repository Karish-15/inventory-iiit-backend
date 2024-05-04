from django.conf import settings
from rest_framework import views, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserTokenSerializer, userRegisterSerializer

class giveUserFromTokenAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        return Response({'status': True, 'message': 'Send POST request to get user details'})
    def post(self, request):
        print(request.user)
        return Response(request.user.username)

class registerUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userRegisterSerializer

class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

class getUserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        if self.request.user.is_admin:
            return User.objects.all()
        return {'error': 'You are not authorized to view this resource'}
    
class isAdminCheck(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        if request.user.is_admin:
            return Response({'status': True, 'message': 'You are an admin'})
        return Response({'status': False, 'message': 'You are not an admin'})