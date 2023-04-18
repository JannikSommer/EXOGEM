import six
import json
import connexion
from openapi_server import util
from datetime import datetime as dt
from openapi_server import db_connection as db_conn
from openapi_server.models.monitor_data import MonitorData  # noqa: E501
from openapi_server.models.memory_information import MemoryInformation  # noqa: E501
from openapi_server.models.server_information import ServerInformation  # noqa: E501


def process_image(monitor_data=None):  # noqa: E501
    """Post a recognition request

     # noqa: E501

    :param image: Image object for processing
    :type image: dict | bytes

    :rtype: 200
    """
    try:
        if connexion.request.is_json:
            monitor_data = MonitorData.from_dict(connexion.request.get_json())  # noqa: E501
    except Exception as e:
        print(e)
        return "Unexpected error with request data.", 500
    try:
        #Create db if does not exist
        conn = db_conn.create_connection("monitor_db.db")

        #Format timing input
        try: 
            total_time = str((monitor_data.response_time - monitor_data.request_time).total_seconds())
            server_process_time = str((monitor_data.server_information.answer_time - monitor_data.server_information.received_time).total_seconds())
            network_request_time = str((monitor_data.server_information.received_time - monitor_data.request_time).total_seconds())
            network_response_time = str((monitor_data.response_time - monitor_data.server_information.answer_time).total_seconds())
        except Exception as e:
            print(e)
            return "Unexpected failure with parsing request data to datetime. Are you using the correct format?", 500

        server_info = monitor_data.server_information
        memory_load = round((monitor_data.server_information.memory_info.used_memory / monitor_data.server_information.memory_info.total_memory) * 100, 2)

        new_timing = (monitor_data.request_id, 
                      monitor_data.client_id, 
                      total_time, 
                      server_process_time,
                      network_request_time,
                      network_response_time,
                      server_info.queue_at_arrival, 
                      server_info.cpu_info, 
                      server_info.gpu_info,
                      memory_load,
                      str(dt.now()))
                      
        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, new_timing)
        db_conn.close_connection(conn)

        return 'Succsess', 200

    except Exception as e:
        print(e)
        return 'Unexpected failure with database.', 500