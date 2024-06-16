import os
from dotenv import load_dotenv
import requests

load_dotenv()

def request_object_detection(request):
  api_url = os.getenv("API_NINJAS_OBJECT_DETECTION_URL")
  
  image_file_descriptor = request["image"]
  
  headers = {
    'X-API-Key': os.getenv("API_NINJAS_KEY")
  }
  
  files = {'image': image_file_descriptor}
  r = requests.post(api_url, files=files, headers=headers)
  
  resObjects = r.json()
  if resObjects:
    resObjectDetected = resObjects[0]["label"]
    return resObjectDetected
  else:
    return None