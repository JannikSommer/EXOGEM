# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MemoryInformation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, total_memory=None, used_memory=None):  # noqa: E501
        """MemoryInformation - a model defined in OpenAPI

        :param total_memory: The total_memory of this MemoryInformation.  # noqa: E501
        :type total_memory: float
        :param used_memory: The used_memory of this MemoryInformation.  # noqa: E501
        :type used_memory: float
        """
        self.openapi_types = {
            'total_memory': float,
            'used_memory': float,

        }

        self.attribute_map = {
            'total_memory': 'total_memory',
            'used_memory': 'used_memory'
        }

        self._total_memory = total_memory
        self._used_memory = used_memory
    

    @classmethod
    def from_dict(cls, dikt) -> 'MemoryInformation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MemoryInformation of this MemoryInformation.  # noqa: E501
        :rtype: MemoryInformation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_memory(self):
        """Gets the total_memory of this MemoryInformation.


        :return: The total_memory of this MemoryInformation.
        :rtype: float
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """Sets the total_memory of this MemoryInformation.


        :param total_memory: The total_memory of this MemoryInformation.
        :type total_memory: float
        """

        self._total_memory = total_memory

    @property
    def used_memory(self):
        """Gets the used_memory of this MemoryInformation.


        :return: The used_memory of this MemoryInformation.
        :rtype: float
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        """Sets the used_memory of this MemoryInformation.


        :param used_memory: The used_memory of this MemoryInformation.
        :type used_memory: float
        """

        self._used_memory = used_memory