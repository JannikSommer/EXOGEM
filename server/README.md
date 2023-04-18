# Introduction 
This is the server application used in the use case of EXOGEM. 

# Getting Started
Make sure you install all the requirements from requirements.txt with 
```pip install -r requirements.txt```

Please note that the installaion process can be tedious with regards to the machine learning implementation. 
For the use case we used a NVIDIA Jetson Nano with the following libraries installed:

1. Python3 v3.6.9
2. Pip3 v21.0.1
3. Tensorflow v2.4.0
5. CUDA v10.2.89
6. cuDNN v8.0.0.180
7. Ubuntu 18.04.5 LTS


# Build and Test
Run the tests with the command 
```python -m unittest discover -v```

# Run the application

Start the python-flask application with 
```python3 -m openapi_server```