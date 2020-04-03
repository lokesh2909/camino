from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from .models import userDetails
from .serializers import detailSerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from rest_framework.response import Response


@csrf_exempt
@parser_classes([JSONParser])
@renderer_classes((JSONRenderer))
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    if request.method == 'POST':
        data = request.data
        if data['name'] == "user1" and data['password'] == "testuser":
            msg = {'message': 'Success'}
            return Response(msg,status=status.HTTP_200_OK)
        else:
            msg = {'error': 'Enter the correct username/password'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@parser_classes([JSONParser])
@renderer_classes((JSONRenderer))
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def create_record(request):
    if request.method == 'POST':
        final_serializer = detailSerializer(data = request.data)
        if final_serializer.is_valid():
            final_serializer.save()
            return Response({'message': 'Record created'},status=status.HTTP_201_CREATED)
        else:
            return Response(final_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        queryset = userDetails.objects.all()
        query_data = serializers.serialize('json',queryset)
        query_data = detailSerializer(queryset, many=True)
        return Response(query_data.data, status=status.HTTP_200_OK)