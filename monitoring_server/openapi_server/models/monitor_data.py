# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.server_information import ServerInformation
from openapi_server import util

from openapi_server.models.server_information import ServerInformation  # noqa: E501

class MonitorData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, request_id=None, client_id=None, server_information=None):  # noqa: E501
        """MonitorData - a model defined in OpenAPI

        :param request_id: The request_id of this MonitorData.  # noqa: E501
        :type request_id: str
        :param client_id: The client_id of this MonitorData.  # noqa: E501
        :type client_id: str
        :param server_information: The server_information of this MonitorData.  # noqa: E501
        :type server_information: ServerInformation
        """
        self.openapi_types = {
            'request_id': str,
            'client_id': str,
            'server_information': ServerInformation,
            'request_time': datetime,
            'response_time': datetime,
        }

        self.attribute_map = {
            'request_id': 'request_id',
            'client_id': 'client_id',
            'server_information': 'server_information',
            'request_time': 'request_time',
            'response_time': 'response_time'
        }

        self._request_id = request_id
        self._client_id = client_id
        self._server_information = server_information
    
        # Will only ignore the properties if the specification has "ignore-time" set to true. Otherwise false.
        if not False:
            self._request_time = datetime.now()
            self._response_time = datetime.now()
    

    @classmethod
    def from_dict(cls, dikt) -> 'MonitorData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MonitorData of this MonitorData.  # noqa: E501
        :rtype: MonitorData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def request_id(self):
        """Gets the request_id of this MonitorData.


        :return: The request_id of this MonitorData.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this MonitorData.


        :param request_id: The request_id of this MonitorData.
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def client_id(self):
        """Gets the client_id of this MonitorData.


        :return: The client_id of this MonitorData.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this MonitorData.


        :param client_id: The client_id of this MonitorData.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def server_information(self):
        """Gets the server_information of this MonitorData.


        :return: The server_information of this MonitorData.
        :rtype: ServerInformation
        """
        return self._server_information

    @server_information.setter
    def server_information(self, server_information):
        """Sets the server_information of this MonitorData.


        :param server_information: The server_information of this MonitorData.
        :type server_information: ServerInformation
        """

        self._server_information = server_information
        
    @property
    def request_time(self):
        """Gets the request_time of this MonitorData.


        :return: The request_time of this MonitorData.
        :rtype: (datetime,)
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this MonitorData.


        :param request_time: The request_time of this MonitorData.
        :type request_time: (datetime,)
        """
        self._request_time= request_time

    @property
    def response_time(self):
        """Gets the response_time of this MonitorData.


        :return: The response_time of this MonitorData.
        :rtype: (datetime,)
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this MonitorData.


        :param response_time: The response_time of this MonitorData.
        :type response_time: (datetime,)
        """
        self._response_time= response_time
