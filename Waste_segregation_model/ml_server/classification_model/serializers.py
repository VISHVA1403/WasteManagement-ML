from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from .models import WasteBinData
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import authenticate

class BinLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteBinData
        fields = '__all__'