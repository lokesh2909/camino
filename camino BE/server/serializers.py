from rest_framework import serializers
from .models import userDetails, users

class loginSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ('name','password')

class detailSerializer(serializers.ModelSerializer):

    class Meta:
        model = userDetails
        fields = ('id','weight')