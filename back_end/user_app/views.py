from django.shortcuts import render
from .models import User_app
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserUpdateSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from django.http import HttpResponse

class Log_in(APIView):
    def post(self, request):
        request.data["username"] = request.data["email"]
        print(request.data)
        user = authenticate(username=request.data["email"],password=request.data["password"])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": {"email": user.email}, "token": token.key})
        else:
            return Response("Something went wrong", status=HTTP_400_BAD_REQUEST)

class Register(APIView):
    def post(self, request):
        request.data["username"] = request.data["email"]
        user = User_app.objects.create_user(**request.data)
        token = Token.objects.create(user=user)
        return Response(
            {"user": {"email": user.email}, "token": token.key}, status=HTTP_201_CREATED
        )

class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "email": user.email,
            "name": user.name,
            "filing_status": user.filing_status,
            "estimated_year_income": user.estimated_year_income,
            "long_term_gains": user.long_term_gains,
            "short_term_gains": user.short_term_gains,
            "contributed_capital": user.contributed_capital,
            "losses": user.losses,
        }
        return Response(user_data)
    
class UpdateUserInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)
