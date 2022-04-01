# PyTorch Flask API + CircleCI

This is CircleCI demo for PyTorch Flask API(Image classification).

![api](https://user-images.githubusercontent.com/8651308/161207011-14665f6d-e08b-48f2-9a66-1dc1dbfc6245.jpg)

## CircleCI features

* [Custom resource class](https://circleci.com/product/features/resource-classes/)(include GPU)
* [CircleCI Runner](https://circleci.com/execution-environments/runner/)(In machine learning project or self-driving projects, there are needs to run build/test/deploy on on-prem machines/devices)
* [SSH debug](https://circleci.com/docs/2.0/ssh-access-jobs/)(Both CircleCI provided machines and runners)
* [Test splitting](https://circleci.com/docs/2.0/parallelism-faster-jobs/)

## How to 

Install the dependencies:

    pipenv install


Run the Flask server:

    FLASK_ENV=development FLASK_APP=app.py flask run

From another tab, send the image file in a request:

    curl -X POST -F file=@images/otter.jpeg http://localhost:5000/predict

