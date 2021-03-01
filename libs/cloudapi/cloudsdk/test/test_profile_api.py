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
from swagger_client.api.profile_api import ProfileApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProfileApi(unittest.TestCase):
    """ProfileApi unit test stubs"""

    def setUp(self):
        self.api = ProfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_profile(self):
        """Test case for create_profile

        Create new Profile  # noqa: E501
        """
        pass

    def test_delete_profile(self):
        """Test case for delete_profile

        Delete Profile  # noqa: E501
        """
        pass

    def test_get_counts_of_equipment_that_use_profiles(self):
        """Test case for get_counts_of_equipment_that_use_profiles

        Get counts of equipment that use specified profiles  # noqa: E501
        """
        pass

    def test_get_profile_by_id(self):
        """Test case for get_profile_by_id

        Get Profile By Id  # noqa: E501
        """
        pass

    def test_get_profile_with_children(self):
        """Test case for get_profile_with_children

        Get Profile and all its associated children  # noqa: E501
        """
        pass

    def test_get_profiles_by_customer_id(self):
        """Test case for get_profiles_by_customer_id

        Get Profiles By customerId  # noqa: E501
        """
        pass

    def test_get_profiles_by_set_of_ids(self):
        """Test case for get_profiles_by_set_of_ids

        Get Profiles By a set of ids  # noqa: E501
        """
        pass

    def test_update_profile(self):
        """Test case for update_profile

        Update Profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
