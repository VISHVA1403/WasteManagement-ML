from django.shortcuts import render
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import joblib
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import WasteBinData, DailyBinSummary, WasteBin
from .serializers import *
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
class SegregationApiView(APIView):
    def post(self, request):
        try:
            data = request.data
            print(data)
            Conductivity = data.get('Conductivity (S/m)')
            moisture = data.get('Moisture Content (%)')
            inductivity = data.get('Inductive Property (H/m)')
            infrared = data.get('Infrared Property (µm)')

            data_frame = np.array([Conductivity, moisture, inductivity, infrared]).reshape(1, -1)
            model = joblib.load('rf_segregation_model.pkl')
            prediction = model.predict(data_frame)
            return Response({'Waste Type': str(prediction[0])}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BinLevel(APIView):
    def post(self, request):
        print(request)
        serializer = BinLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"wastebin": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        queryset = WasteBinData.objects.all().filter(bin = pk)
        serializer = BinLevelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request):
        queryset = WasteBinData.objects.all().order_by("-id")
        serializer = BinLevelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WeeklyLevelApiView(APIView):
    def get(self, request):
        queryset = DailyBinSummary.objects.all().order_by("-id")
        serializer = WeeklyBinLevelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BinDetailAPIView(generics.ListCreateAPIView):
    queryset = WasteBin.objects.all()
    serializer_class = WasteBinSerializer
    permission_classes = [IsAuthenticated]

class NodeChecking(APIView):
    def post(self, request):
        print(request.data)
        return Response("hii", status=status.HTTP_100_CONTINUE)

    def get(self, request):
        print("hii")
        return Response({'hii': "hii"}, status=status.HTTP_200_OK)

# myapp/views.py



User = get_user_model()

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        # Overriding the create method to handle the password validation
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user =serializer.validated_data['user']
            token,created =Token.objects.get_or_create(user=user)
            print(token.key)
            return Response(token.key  , status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
