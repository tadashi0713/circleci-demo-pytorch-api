from io import BytesIO
import pytest
from app import app

def test_giant_panda():
  with open('./images/giant_panda.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'giant_panda.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'giant_panda'
