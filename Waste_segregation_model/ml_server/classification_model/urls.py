from django.urls import path
from .views import *
urlpatterns = [
    path('classification/', SegregationApiView.as_view(), name='Classification_model'),
    path('binlevel/',BinLevel.as_view(),name = 'binlevel'),
    path('binlevel/<str:pk>',BinLevel.as_view(),name = 'getbinlevel'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('WasteBins/',BinDetailAPIView.as_view(),name='BinDetail'),
    path('Weekly/',WeeklyLevelApiView.as_view(),name='weekly level'),
    path('',NodeChecking.as_view()),
]
