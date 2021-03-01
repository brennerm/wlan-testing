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

class ApSsidMetrics(object):
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
        'ssid_stats': 'ListOfSsidStatisticsPerRadioMap'
    }

    attribute_map = {
        'model_type': 'model_type',
        'ssid_stats': 'ssidStats'
    }

    def __init__(self, model_type=None, ssid_stats=None):  # noqa: E501
        """ApSsidMetrics - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._ssid_stats = None
        self.discriminator = None
        self.model_type = model_type
        if ssid_stats is not None:
            self.ssid_stats = ssid_stats

    @property
    def model_type(self):
        """Gets the model_type of this ApSsidMetrics.  # noqa: E501


        :return: The model_type of this ApSsidMetrics.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ApSsidMetrics.


        :param model_type: The model_type of this ApSsidMetrics.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def ssid_stats(self):
        """Gets the ssid_stats of this ApSsidMetrics.  # noqa: E501


        :return: The ssid_stats of this ApSsidMetrics.  # noqa: E501
        :rtype: ListOfSsidStatisticsPerRadioMap
        """
        return self._ssid_stats

    @ssid_stats.setter
    def ssid_stats(self, ssid_stats):
        """Sets the ssid_stats of this ApSsidMetrics.


        :param ssid_stats: The ssid_stats of this ApSsidMetrics.  # noqa: E501
        :type: ListOfSsidStatisticsPerRadioMap
        """

        self._ssid_stats = ssid_stats

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
        if issubclass(ApSsidMetrics, dict):
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
        if not isinstance(other, ApSsidMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
