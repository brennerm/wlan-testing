# coding: utf-8

"""
    CloudSDK Portal API

    APIs that provide services for provisioning, monitoring, and history retrieval of various data elements of CloudSDK.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ServiceAdoptionMetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_adoption_metrics_all_per_day(self, year, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_day(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_all_per_day_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_all_per_day_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_all_per_day_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_day_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_all_per_day" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_all_per_day`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/allPerDay', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_adoption_metrics_all_per_month(self, year, **kwargs):  # noqa: E501
        """Get monthly service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_month(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_all_per_month_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_all_per_month_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_all_per_month_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get monthly service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_month_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_all_per_month" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_all_per_month`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/allPerMonth', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_adoption_metrics_all_per_week(self, year, **kwargs):  # noqa: E501
        """Get weekly service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_week(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_all_per_week_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_all_per_week_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_all_per_week_with_http_info(self, year, **kwargs):  # noqa: E501
        """Get weekly service adoption metrics for a given year  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_all_per_week_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_all_per_week" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_all_per_week`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/allPerWeek', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_adoption_metrics_per_customer_per_day(self, year, customer_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year aggregated by customer and filtered by specified customer ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_customer_per_day(year, customer_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] customer_ids: filter by customer ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_per_customer_per_day_with_http_info(year, customer_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_per_customer_per_day_with_http_info(year, customer_ids, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_per_customer_per_day_with_http_info(self, year, customer_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year aggregated by customer and filtered by specified customer ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_customer_per_day_with_http_info(year, customer_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] customer_ids: filter by customer ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'customer_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_per_customer_per_day" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_per_customer_per_day`")  # noqa: E501
        # verify the required parameter 'customer_ids' is set
        if ('customer_ids' not in params or
                params['customer_ids'] is None):
            raise ValueError("Missing the required parameter `customer_ids` when calling `get_adoption_metrics_per_customer_per_day`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'customer_ids' in params:
            query_params.append(('customerIds', params['customer_ids']))  # noqa: E501
            collection_formats['customerIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/perCustomerPerDay', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_adoption_metrics_per_equipment_per_day(self, year, equipment_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year filtered by specified equipment ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_equipment_per_day(year, equipment_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] equipment_ids: filter by equipment ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_per_equipment_per_day_with_http_info(year, equipment_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_per_equipment_per_day_with_http_info(year, equipment_ids, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_per_equipment_per_day_with_http_info(self, year, equipment_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year filtered by specified equipment ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_equipment_per_day_with_http_info(year, equipment_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] equipment_ids: filter by equipment ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'equipment_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_per_equipment_per_day" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_per_equipment_per_day`")  # noqa: E501
        # verify the required parameter 'equipment_ids' is set
        if ('equipment_ids' not in params or
                params['equipment_ids'] is None):
            raise ValueError("Missing the required parameter `equipment_ids` when calling `get_adoption_metrics_per_equipment_per_day`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'equipment_ids' in params:
            query_params.append(('equipmentIds', params['equipment_ids']))  # noqa: E501
            collection_formats['equipmentIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/perEquipmentPerDay', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_adoption_metrics_per_location_per_day(self, year, location_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year aggregated by location and filtered by specified location ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_location_per_day(year, location_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] location_ids: filter by location ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_adoption_metrics_per_location_per_day_with_http_info(year, location_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_adoption_metrics_per_location_per_day_with_http_info(year, location_ids, **kwargs)  # noqa: E501
            return data

    def get_adoption_metrics_per_location_per_day_with_http_info(self, year, location_ids, **kwargs):  # noqa: E501
        """Get daily service adoption metrics for a given year aggregated by location and filtered by specified location ids  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_adoption_metrics_per_location_per_day_with_http_info(year, location_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: (required)
        :param list[int] location_ids: filter by location ids. (required)
        :return: list[ServiceAdoptionMetrics]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'location_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_adoption_metrics_per_location_per_day" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_adoption_metrics_per_location_per_day`")  # noqa: E501
        # verify the required parameter 'location_ids' is set
        if ('location_ids' not in params or
                params['location_ids'] is None):
            raise ValueError("Missing the required parameter `location_ids` when calling `get_adoption_metrics_per_location_per_day`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'location_ids' in params:
            query_params.append(('locationIds', params['location_ids']))  # noqa: E501
            collection_formats['locationIds'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tip_wlan_ts_auth']  # noqa: E501

        return self.api_client.call_api(
            '/portal/adoptionMetrics/perLocationPerDay', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ServiceAdoptionMetrics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
