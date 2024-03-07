from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from .models import WasteBinData,WasteBin,DailyBinSummary
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class BinLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteBinData
        fields = '__all__'

class WeeklyBinLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyBinSummary
        fields = '__all__'

class WasteBinSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteBin
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        print(data)
        username = data.get('username')
        password = data.get('password')
        print(username)
        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Incorrect credentials. Please try again.")

        else:
            raise serializers.ValidationError("Both username and password are required.")

        return data