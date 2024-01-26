from django.shortcuts import render
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import joblib
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import WasteBinData, DailyBinSummary,WasteBin
from .serializers import *
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

class Binlevel(APIView):

    def post(self,request):
        serializer = BinLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "wastebin": serializer.data
                             }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def get(self, request, pk):
        try:
            waste_bin_data = WasteBinData.objects.get(pk=pk)
            serializer = BinLevelSerializer(waste_bin_data)
            return Response({"wastebin": serializer.data}, status=status.HTTP_200_OK)
        except WasteBinData.DoesNotExist:
            return Response({"error": "WasteBinData not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,request):
        queryset = WasteBinData.objects.all().order_by("-id")
        serializer = BinLevelSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class nodechecking(APIView):
    def post(self,request):
        print(request)
        return Response("hii",status=status.HTTP_100_CONTINUE)
    def get(self,request):
        print("hii")
        return Response({'hii':"hii"},status=status.HTTP_200_OK)
 