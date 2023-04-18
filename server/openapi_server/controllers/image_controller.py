import six
import cv2
import connexion
import numpy as np
from jtop import jtop
from datetime import datetime 
from datetime import timezone
from openapi_server import util
from process_image import ProcessImage
from openapi_server import global_vars
from multiprocessing import Process, Lock
from openapi_server.models.monitor_data import MonitorData
from openapi_server.models.server_information import ServerInformation
from openapi_server.models.memory_information import MemoryInformation

PI = ProcessImage()

def process_image(location = None, image_data = None):  # noqa: E501
    """Post a recognition request

     # noqa: E501

    :param location: Name of the location from which the image_data comes from
    :type location: str
    :param image_data: The base64 string of the image_data
    :type image_data: str

    :rtype: dict of response_data and monitor_data
    """
    # Timestamp for beginning the processing of the request. 
    received_at = datetime.now().replace(tzinfo=timezone.utc)

    active_thread_number = 0 
    with global_vars.thread_count_mutex:
        global_vars.ACTIVE_THREAD_COUNT += 1
        active_thread_number = global_vars.ACTIVE_THREAD_COUNT
    
    # Receiving the image data and ID. 
    image_data = connexion.request.form["image_data"]
    location = connexion.request.form["location"]

    #Get server information before processing the image
    try:
        with global_vars.sys_info_mutex:
            cpu_load, gpu_load, memory_info = global_vars.SYSTEM_INFO.retrieve_data()
    except Exception as e:
        print(e)
        cpu_load = 0
        gpu_load = 0
        memory_info = MemoryInformation(0,0)
        
    # Begin processing the image
    results = process_image_data(image_data)
    if len(results) > 0:
        for name, accuracy in results:
            print("ALARM! At location " + str(location) + ", the perp " + str(name) + ", was recognized with an accuracy of " + str(accuracy))

    # Gather all params for server information
    process_completed_at = datetime.now().replace(tzinfo=timezone.utc)
    server_information = ServerInformation(received_at, process_completed_at, active_thread_number, cpu_load, gpu_load, memory_info)

    # Prepare monitordata
    response_data = "The request went well" # Place return data here.
    monitor_data = MonitorData(server_information=server_information)
    return_data = {"response_data": response_data, "monitor_data": monitor_data}

    with global_vars.thread_count_mutex:
        global_vars.ACTIVE_THREAD_COUNT -= 1

    return return_data, 200


def process_image_data(image_data):
    """ Uses process_image.py to process the image_data received

        :param image_data: base64 string of the image
        :type image_data: str

        :rtype: list
    """
    image_decoded = PI.decode_image(image_data)
    image_np = np.frombuffer(image_decoded, dtype=np.uint8)
    image_cv2 = cv2.imdecode(image_np, flags=1)
    return PI.is_wanted(image_cv2)
