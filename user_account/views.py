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