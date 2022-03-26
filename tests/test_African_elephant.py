from io import BytesIO
import pytest
from app import app

def test_African_elephant():
  with open('./images/African_elephant.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'African_elephant.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'African_elephant'
