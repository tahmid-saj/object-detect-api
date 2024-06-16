from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, status, mixins, viewsets

from django.shortcuts import render, get_object_or_404

from object_detector.permissions import AdminOrReadOnly, AdminOnly
from object_detector.controllers import get_object_detection_response

# Create your views here.

class ObjectDetectionResponse(APIView):
  # permission_classes = [AdminOrReadOnly]
  
  def post(self, request):
    response = get_object_detection_response(request=request)
    
    return Response(data=response)