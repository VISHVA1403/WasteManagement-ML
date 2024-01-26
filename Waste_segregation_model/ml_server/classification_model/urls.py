from django.urls import path
from .views import *
urlpatterns = [
    path('classification/', SegregationApiView.as_view(), name='Classification_model'),
    path('binlevel/',Binlevel.as_view(),name = 'binlevel'),
    path('binlevel/<str:pk>',Binlevel.as_view(),name = 'getbinlevel'),
    path('',nodechecking.as_view())
]
