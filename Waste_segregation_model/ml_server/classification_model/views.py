from django.shortcuts import render
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import joblib

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

"""from django.shortcuts import render
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import joblib

class SegregationApiView(APIView):
    def post(self, request):
        try:
            data = request.data

            Conductivity = data.get('Conductivity (S/m)')
            moisture = data.get('Moisture Content (%)')
            inductivity = data.get('Inductive Property (H/m)')
            infrared = data.get('Infrared Property (µm)')

            data_frame = np.array([Conductivity, moisture, inductivity, infrared]).reshape(1, -1)

            model = joblib.load('rf_segregation_model.pkl')
            prediction = model.predict(data_frame)

            return Response({'Waste Type': str(prediction[0])}, status=status.HTTP_200_OK)
        except Exception as e: # Debugging line
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
"""