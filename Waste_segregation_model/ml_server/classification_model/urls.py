from django.urls import path
from .views import SegregationApiView
urlpatterns = [
    path('classification/', SegregationApiView.as_view(), name='Classification_model'),
]
