from utils.api_requests.object_detection_requests import request_object_detection

def get_object_detection_response(request):
  request = request.data
  print(request)
  
  object_detection_response = request_object_detection(request)
  
  response = {
    "foodObject": object_detection_response
  }
  
  return response