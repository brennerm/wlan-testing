# coding: utf-8

"""
    CloudSDK Portal API

    APIs that provide services for provisioning, monitoring, and history retrieval of various data elements of CloudSDK.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LocationDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'model_type': 'str',
        'country_code': 'CountryCode',
        'daily_activity_details': 'LocationActivityDetailsMap',
        'maintenance_window': 'DaysOfWeekTimeRangeSchedule',
        'rrm_enabled': 'bool'
    }

    attribute_map = {
        'model_type': 'model_type',
        'country_code': 'countryCode',
        'daily_activity_details': 'dailyActivityDetails',
        'maintenance_window': 'maintenanceWindow',
        'rrm_enabled': 'rrmEnabled'
    }

    def __init__(self, model_type=None, country_code=None, daily_activity_details=None, maintenance_window=None, rrm_enabled=None):  # noqa: E501
        """LocationDetails - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._country_code = None
        self._daily_activity_details = None
        self._maintenance_window = None
        self._rrm_enabled = None
        self.discriminator = None
        if model_type is not None:
            self.model_type = model_type
        if country_code is not None:
            self.country_code = country_code
        if daily_activity_details is not None:
            self.daily_activity_details = daily_activity_details
        if maintenance_window is not None:
            self.maintenance_window = maintenance_window
        if rrm_enabled is not None:
            self.rrm_enabled = rrm_enabled

    @property
    def model_type(self):
        """Gets the model_type of this LocationDetails.  # noqa: E501


        :return: The model_type of this LocationDetails.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this LocationDetails.


        :param model_type: The model_type of this LocationDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["LocationDetails"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def country_code(self):
        """Gets the country_code of this LocationDetails.  # noqa: E501


        :return: The country_code of this LocationDetails.  # noqa: E501
        :rtype: CountryCode
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this LocationDetails.


        :param country_code: The country_code of this LocationDetails.  # noqa: E501
        :type: CountryCode
        """

        self._country_code = country_code

    @property
    def daily_activity_details(self):
        """Gets the daily_activity_details of this LocationDetails.  # noqa: E501


        :return: The daily_activity_details of this LocationDetails.  # noqa: E501
        :rtype: LocationActivityDetailsMap
        """
        return self._daily_activity_details

    @daily_activity_details.setter
    def daily_activity_details(self, daily_activity_details):
        """Sets the daily_activity_details of this LocationDetails.


        :param daily_activity_details: The daily_activity_details of this LocationDetails.  # noqa: E501
        :type: LocationActivityDetailsMap
        """

        self._daily_activity_details = daily_activity_details

    @property
    def maintenance_window(self):
        """Gets the maintenance_window of this LocationDetails.  # noqa: E501


        :return: The maintenance_window of this LocationDetails.  # noqa: E501
        :rtype: DaysOfWeekTimeRangeSchedule
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """Sets the maintenance_window of this LocationDetails.


        :param maintenance_window: The maintenance_window of this LocationDetails.  # noqa: E501
        :type: DaysOfWeekTimeRangeSchedule
        """

        self._maintenance_window = maintenance_window

    @property
    def rrm_enabled(self):
        """Gets the rrm_enabled of this LocationDetails.  # noqa: E501


        :return: The rrm_enabled of this LocationDetails.  # noqa: E501
        :rtype: bool
        """
        return self._rrm_enabled

    @rrm_enabled.setter
    def rrm_enabled(self, rrm_enabled):
        """Sets the rrm_enabled of this LocationDetails.


        :param rrm_enabled: The rrm_enabled of this LocationDetails.  # noqa: E501
        :type: bool
        """

        self._rrm_enabled = rrm_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LocationDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LocationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
