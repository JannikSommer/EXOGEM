import base64
from typing import List
import openapi_client
from openapi_client.api import image_api
from openapi_client import ApiClient
from openapi_client import ApiException
from openapi_client import Configuration
from openapi_client.model.monitor_data import MonitorData
class ProcessNodeInterface:
    """
    Provides capabilities send images to processing nodes.
    """
    def __init__(self, host: str = "https://project.sommersoftware.dk") -> None:
        self._configuration = Configuration(
            host = host
        )
        self._api_instance = image_api.ImageApi(
            ApiClient(self._configuration)
        )

    def process_image(self, image_data: str, location: str, monitor_data: MonitorData) -> None:
        """
        Sends an image processing request to the processing node.
        """
        try:
            # Post a recognition request
            response = self._api_instance.process_image(
                image_data = image_data,
                location = location,
                monitor_data = monitor_data
            )
        except ApiException as e:
            print("Exception when calling ImageApi->process_image: %s\n" % e)

    @classmethod
    def encode_image(self, image: bytes) -> str:
        """
        Encode and convert bytes into base64 string.
        """
        s = str(base64.b64encode(image))
        return s[2:len(s)-1]

    @classmethod
    def decode_image(self, image: str) -> bytes:
        """
        Decode and convert base64 string into bytes.
        """
        return base64.b64decode(image)