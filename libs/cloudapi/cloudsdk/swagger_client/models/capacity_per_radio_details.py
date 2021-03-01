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

class CapacityPerRadioDetails(object):
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
        'total_capacity': 'int',
        'available_capacity': 'MinMaxAvgValueInt',
        'unavailable_capacity': 'MinMaxAvgValueInt',
        'used_capacity': 'MinMaxAvgValueInt',
        'unused_capacity': 'MinMaxAvgValueInt'
    }

    attribute_map = {
        'total_capacity': 'totalCapacity',
        'available_capacity': 'availableCapacity',
        'unavailable_capacity': 'unavailableCapacity',
        'used_capacity': 'usedCapacity',
        'unused_capacity': 'unusedCapacity'
    }

    def __init__(self, total_capacity=None, available_capacity=None, unavailable_capacity=None, used_capacity=None, unused_capacity=None):  # noqa: E501
        """CapacityPerRadioDetails - a model defined in Swagger"""  # noqa: E501
        self._total_capacity = None
        self._available_capacity = None
        self._unavailable_capacity = None
        self._used_capacity = None
        self._unused_capacity = None
        self.discriminator = None
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if available_capacity is not None:
            self.available_capacity = available_capacity
        if unavailable_capacity is not None:
            self.unavailable_capacity = unavailable_capacity
        if used_capacity is not None:
            self.used_capacity = used_capacity
        if unused_capacity is not None:
            self.unused_capacity = unused_capacity

    @property
    def total_capacity(self):
        """Gets the total_capacity of this CapacityPerRadioDetails.  # noqa: E501


        :return: The total_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :rtype: int
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this CapacityPerRadioDetails.


        :param total_capacity: The total_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :type: int
        """

        self._total_capacity = total_capacity

    @property
    def available_capacity(self):
        """Gets the available_capacity of this CapacityPerRadioDetails.  # noqa: E501


        :return: The available_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity):
        """Sets the available_capacity of this CapacityPerRadioDetails.


        :param available_capacity: The available_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._available_capacity = available_capacity

    @property
    def unavailable_capacity(self):
        """Gets the unavailable_capacity of this CapacityPerRadioDetails.  # noqa: E501


        :return: The unavailable_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._unavailable_capacity

    @unavailable_capacity.setter
    def unavailable_capacity(self, unavailable_capacity):
        """Sets the unavailable_capacity of this CapacityPerRadioDetails.


        :param unavailable_capacity: The unavailable_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._unavailable_capacity = unavailable_capacity

    @property
    def used_capacity(self):
        """Gets the used_capacity of this CapacityPerRadioDetails.  # noqa: E501


        :return: The used_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        """Sets the used_capacity of this CapacityPerRadioDetails.


        :param used_capacity: The used_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._used_capacity = used_capacity

    @property
    def unused_capacity(self):
        """Gets the unused_capacity of this CapacityPerRadioDetails.  # noqa: E501


        :return: The unused_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._unused_capacity

    @unused_capacity.setter
    def unused_capacity(self, unused_capacity):
        """Sets the unused_capacity of this CapacityPerRadioDetails.


        :param unused_capacity: The unused_capacity of this CapacityPerRadioDetails.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._unused_capacity = unused_capacity

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
        if issubclass(CapacityPerRadioDetails, dict):
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
        if not isinstance(other, CapacityPerRadioDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
