#!/usr/bin/env python3
import os
import cv2
import connexion
from threading import Timer
from openapi_server import encoder
from openapi_server import global_vars
from process_image import ProcessImage
from multiprocessing import Process, Lock
from openapi_server.controllers.image_controller import process_image_data

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'EXOGEM'},
                pythonic_params=True)
    update_sys_information()
    start_tensorflow()
    app.run(port=8080)

def start_tensorflow() -> None:
    """Start the machine learning implementation before accepting requests 
       (Removes long processing time of first request)
    """
    print("Starting tensorflow...")
    image_path = os.path.join(os.getcwd(), "resources", "000001.jpg")
    print(image_path)
    image = cv2.imread(image_path)
    image_png = cv2.imencode('.png', image)[1]
    image_data = ProcessImage.encode_image(image_png)
    process_image_data(image_data)
    print("Tensorflow started.")

def update_sys_information() -> None:
    """
    Gathers the system resournce information and saves it to a shared data structure.
    This function is repeated every 1 second. 
    """
    #Run the function every 1 second
    Timer(1.0, update_sys_information).start()
    #Gather the system resource information
    cpu_load, gpu_load, mem_info = global_vars.SYSTEM_INFO.gather_data()

    #With the specific mutex, update the values and release lock
    with global_vars.sys_info_mutex:
        global_vars.SYSTEM_INFO.update_info(cpu_load, gpu_load, mem_info)

if __name__ == '__main__':
    #init global variables for use in image_controller
    global_vars.initialize()
    main()
