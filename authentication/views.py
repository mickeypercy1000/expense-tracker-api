# from rest_framework.decorators import api_view
from user.models import User
from authentication.serializers import CreateUserSerializer, LoginSerializer, LogoutUserSerializer, UpdateRetrieveUserSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.http import Http404
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.
class CreateUser(generics.CreateAPIView):
    '''
    This endpoint creates a new user and returns appropriate responses.
    '''
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            response_data = serializer.data
            message = {
                "id": response_data.get("id"),
                "email": response_data.get("email"),
                "message": "User created successfully"
            }
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception:
            message = {"message": "Unable to create user"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)            


class LoginUser(generics.CreateAPIView):
    '''
    This endpoint validates login credentials(email and password) and returns responses
    '''
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        try:
            refresh = RefreshToken.for_user(user)

            return Response({
                "id": user.id,
                "email": user.email,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_200_OK)
        except Exception:
            message = {"message": "login failed"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)   


class GetUserByID(generics.RetrieveAPIView, generics.UpdateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UpdateRetrieveUserSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            email = instance.get_email()
            new_email = instance.email
            print("emailllllll", email, new_email)
        except Http404:
            message = {"message": "User not found."}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.get_serializer(instance)
            return Response({"user": serializer.data}, status=status.HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutUser(generics.GenericAPIView):

    serializer_class = LogoutUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        message = {"message": "Logout successful"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)






