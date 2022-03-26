from io import BytesIO
import pytest
from app import app

def test_wood_rabbit():
  with open('./images/wood_rabbit.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'wood_rabbit.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'wood_rabbit'
