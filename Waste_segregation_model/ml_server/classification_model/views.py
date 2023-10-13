from django.shortcuts import render
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import joblib
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .serializers import RegisterSerializer,LoginSerializer
class SegregationApiView(APIView):
    def post(self, request):
        try:
            data = request.data
            Conductivity= data.get('Conductivity (S/m)')
            moisture = data.get('Moisture Content (%)')
            inductivity = data.get('Inductive Property (H/m)')
            infrared = data.get('Infrared Property (µm)')

            data_frame = np.array([Conductivity,moisture,inductivity,infrared]).reshape(1,-1)
            model = joblib.load('rf_segregation_model.pkl')
            prediction = model.predict(data_frame)
            return Response({'Waste Type':str(prediction[0])},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    def post(self,request):
        serializer = LoginSerializer(request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user=user)
            return Response({'token': str(token.access_token)},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)