"""
    Process Node Rest Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


from openapi_client.models import MonitorData


class ImageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __process_image(
            self,
            image_data,
            location,
            monitor_data = None,
            choke_monitor = False,
            **kwargs
        ):
            """Post a recognition request  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.process_image(image_data, location, async_req=True)
            >>> result = thread.get()

            Args:
                image_data (str):
                location (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """


            
            monitor_params = {'url': api_client.configuration.get_monitor_url(),
                            'ignore_time': False,
                            'ignore_client_id': False,
                            'choke_monitor': choke_monitor,
                            'resource_path': self.settings["endpoint_path"],
                            'datatype' : type(MonitorData()) }
            

            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            

            kwargs['image_data'] = \
                image_data
            kwargs['location'] = \
                location
            
            if monitor_params['url'] is not None:
                return self.call_with_http_info(monitor_params, monitor_data, **kwargs)
            else:
                return self.call_with_http_info(**kwargs)
        self.process_image = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/image',
                'operation_id': 'process_image',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'image_data',
                    'location',
                ],
                'required': [
                    'image_data',
                    'location',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'image_data':
                        (str,),
                    'location':
                        (str,),
                },
                'attribute_map': {
                    'image_data': 'image_data',
                    'location': 'location',
                },
                'location_map': {
                    'image_data': 'form',
                    'location': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__process_image,
        )

    def send_monitor_data(self, monitor_data):
        monitor_params = {'url': self.api_client.configuration.get_monitor_url(),
                            'ignore_time': False,
                            'resource_path': self.process_image.settings["endpoint_path"]
                        }
        self.api_client.send_monitor_data(monitor_params, monitor_data)
