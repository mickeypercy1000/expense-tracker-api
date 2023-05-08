from audioop import add
from authentication.serializers import CreateUserSerializer
from user.models import Expenditure, Income
from user.serializers import ExpenditureSerializer, IncomeSerializer
from user.models import User
from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from django.http import Http404


class UserIncome(generics.CreateAPIView, generics.GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get(self, *args, **kwargs):
        '''
        This function fetches all income for a given user - getUserIncome"
        '''
        try:
            if self.request.user.is_authenticated:
                user_id = self.request.user.id
                user_income = Income.objects.filter(user=user_id)
                if user_income:
                    income = IncomeSerializer(user_income, many=True).data
                    return Response({"income": income}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User has no income."}, status=status.HTTP_404_NOT_FOUND)
            return Response({"message": "Login required."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response({"message": "Could not fetch user income data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        '''
        This function creates a new income for a given user- addUserIncome"
        '''
        try:
            request = self.request
            if request.user.is_authenticated:
                user = request.user
                income = serializer.save(user=user)
                serializer = IncomeSerializer(instance=income)
                return Response({"income": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"message": "Unable to create user income"}, status=status.HTTP_400_BAD_REQUEST)


class GetIncomeByID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        '''
        This function fetches income by ID - getIncome"
        '''
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "income not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.get_serializer(instance)
        except Exception:
            return Response({"message": "Sorry, there was an error while retrieving income"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"income": serializer.data}, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        '''
        This function updates income by ID - updateIncomeByID"
        '''
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "income not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = IncomeSerializer(instance, data=request.data, required_fields=[''])
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as error:
            return Response({"message": error.detail}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"income": serializer.data}, status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "income not found."}, status=status.HTTP_404_NOT_FOUND)
        try:
            instance.delete()
        except Exception as e:
            return Response({"message": "There was an error while trying to delete the income"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": "income deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class UserExpenditure(generics.CreateAPIView, generics.GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

    def get(self, *args, **kwargs):
        '''
        This function fetches all the expenditure for a given user - getUserExpenditure"
        '''
        try:
            if self.request.user.is_authenticated:
                user_id = self.request.user.id
                user_expenditure = Expenditure.objects.filter(user=user_id)
                if user_expenditure:
                    expenditure = ExpenditureSerializer(user_expenditure, many=True).data
                    return Response({"expenditure": expenditure}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User has no expenditure."}, status=status.HTTP_404_NOT_FOUND)
            return Response({"message": "Login required."}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response({"message": "Could not fetch user expenditure data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        '''
        This function creates a new expenditure for a given user- addUserExpenditure"
        '''
        try:
            request = self.request
            if request.user.is_authenticated:
                user = request.user
                expenditure = serializer.save(user=user)
                serializer = IncomeSerializer(instance=expenditure)
                return Response({"expenditure": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"message": "Unable to create user expenditure"}, status=status.HTTP_400_BAD_REQUEST)


class GetExpenditureByID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        '''
        This function fetches expenditure by ID - getExpenditure"
        '''
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "expenditure not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = self.get_serializer(instance)
        except Exception:
            return Response({"message": "Sorry, there was an error while retrieving expenditure"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"expenditure": serializer.data}, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        '''
        This function updates expenditure by ID - updateExpenditureByID"
        '''
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "expenditure not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenditureSerializer(instance, data=request.data, required_fields=[''])
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as error:
            return Response({"message": error.detail}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"expenditure": serializer.data}, status=status.HTTP_200_OK)


    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({"message": "expenditure not found."}, status=status.HTTP_404_NOT_FOUND)
        try:
            instance.delete()
        except Exception:
            return Response({"message": "There was an error while trying to delete the expenditure."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": "expenditure deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class GetAllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer