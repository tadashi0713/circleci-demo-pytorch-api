from io import BytesIO
import pytest
from app import app

def test_beagle():
  with open('./images/beagle.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'beagle.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'beagle'
