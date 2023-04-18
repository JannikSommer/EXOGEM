from multiprocessing import Process, Lock
from openapi_server.system_resource_information import SystemResourceInformaton

def initialize(): 
    global ACTIVE_THREAD_COUNT
    ACTIVE_THREAD_COUNT = 0
    global thread_count_mutex
    thread_count_mutex = Lock()
    global sys_info_mutex
    sys_info_mutex = Lock()
    global SYSTEM_INFO
    SYSTEM_INFO = SystemResourceInformaton()
