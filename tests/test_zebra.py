from io import BytesIO
import pytest
from app import app

def test_zeebra():
  with open('./images/zebra.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'zebra.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'horse'
