from jtop import jtop
from openapi_server.models.memory_information import MemoryInformation

class SystemResourceInformaton:
    def __init__(self):
        self.cpu_load = 0
        self.gpu_load = 0
        self.mem_info = MemoryInformation(0,0)

    def perpare_data(self):
        return self.get_server_information()

    def update_info(self, cpu_load, gpu_load, mem_info):
        self.cpu_load = cpu_load
        self.gpu_load = gpu_load
        self.mem_info = mem_info

    def retrieve_data(self):
        return self.cpu_load, self.gpu_load, self.mem_info

    def get_server_information(self):
        """Uses jtop to get system information

        :rtype: triple(cpu_load, gpu_load, memory_info) 
        """
        jetson = jtop()
        jetson.start()
        cpus = jetson.cpu
        gpu = jetson.gpu
        memory = jetson.ram
        jetson.close()

        # Get CPU resource information
        cpu_load_total = 0
        cpu_count = 0
        for k in cpus:
            cpu_count += 1
            cpu_load_total = cpu_load_total + cpus[k]["val"]
        cpu_load = cpu_load_total / cpu_count

        # Get GPU resource information
        gpu = jetson.gpu
        gpu_load = gpu["val"]

        # Get memory resource information
        memory = jetson.ram
        memory_info = MemoryInformation(memory["tot"], memory["use"])

        return cpu_load, gpu_load, memory_info