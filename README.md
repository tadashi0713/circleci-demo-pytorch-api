# PyTorch Flask API + CircleCI

This is CircleCI demo for PyTorch Flask API(Image classification).

## CircleCI features

* Custom resource class(include GPU)
* CircleCI Runner(In machine learning project or self-driving projects, there are needs to run build/test/deploy on on-prem machines/devices)
* SSH debug(Both CircleCI provided machines and runners)
* 

## How to 

Install the dependencies:

    pipenv install


Run the Flask server:

    FLASK_ENV=development FLASK_APP=app.py flask run

From another tab, send the image file in a request:

    curl -X POST -F file=@images/otter.jpeg http://localhost:5000/predict

