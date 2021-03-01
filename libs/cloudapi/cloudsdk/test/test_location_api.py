# coding: utf-8

"""
    CloudSDK Portal API

    APIs that provide services for provisioning, monitoring, and history retrieval of various data elements of CloudSDK.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.location_api import LocationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLocationApi(unittest.TestCase):
    """LocationApi unit test stubs"""

    def setUp(self):
        self.api = LocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_location(self):
        """Test case for create_location

        Create new Location  # noqa: E501
        """
        pass

    def test_delete_location(self):
        """Test case for delete_location

        Delete Location  # noqa: E501
        """
        pass

    def test_get_location_by_id(self):
        """Test case for get_location_by_id

        Get Location By Id  # noqa: E501
        """
        pass

    def test_get_location_by_set_of_ids(self):
        """Test case for get_location_by_set_of_ids

        Get Locations By a set of ids  # noqa: E501
        """
        pass

    def test_get_locations_by_customer_id(self):
        """Test case for get_locations_by_customer_id

        Get Locations By customerId  # noqa: E501
        """
        pass

    def test_update_location(self):
        """Test case for update_location

        Update Location  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
