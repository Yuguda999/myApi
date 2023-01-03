from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
def api_routes(request):
    routes = [
        'GET /api/users',
        'GET /api/users/id',
        'POST /api/signup',
        'POST /api/login',
        'PUT /api/change-password',
        'PUT /api/update-profile/id',
        'DELETE /api/delete/id',
        'DELETE /api/delete-all',
    ]
    return Response(routes)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_users_by_id(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponse({'user not found'}, status=404)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


class LoginUser(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePassword(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfile(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class DeleteAccount(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user.delete()
        return Response({"result": "user delete"})


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_all_users(request):
    users = User.objects.all()
    users.delete()
    return Response({'result': 'deleted all users'})
