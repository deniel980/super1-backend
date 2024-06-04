from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class FavouriteCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteCountry
        fields = '__all__'
