from django.urls import path, include
from object_detector.views import ObjectDetectionResponse

urlpatterns = [
  path("object_detection/", ObjectDetectionResponse.as_view(), name="object-detection-response")
]
