from io import BytesIO
import pytest
from app import app

def test_tiger_cat():
  with open('./images/tiger_cat.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'tiger_cat.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'tiger_cat'
