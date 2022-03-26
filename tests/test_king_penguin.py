from io import BytesIO
import pytest
from app import app

def test_king_penguin():
  with open('./images/king_penguin.jpeg', 'rb') as img:
    img_string = BytesIO(img.read())
  response = app.test_client().post('/predict', data={'file': (img_string, 'king_penguin.jpeg')},
                      content_type="multipart/form-data")
  assert response.json['class_name'] == 'king_penguin'
