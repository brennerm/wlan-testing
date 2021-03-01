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

class MinMaxAvgValueIntPerRadioMap(object):
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
        'is5_g_hz': 'MinMaxAvgValueInt',
        'is5_g_hz_u': 'MinMaxAvgValueInt',
        'is5_g_hz_l': 'MinMaxAvgValueInt',
        'is2dot4_g_hz': 'MinMaxAvgValueInt'
    }

    attribute_map = {
        'is5_g_hz': 'is5GHz',
        'is5_g_hz_u': 'is5GHzU',
        'is5_g_hz_l': 'is5GHzL',
        'is2dot4_g_hz': 'is2dot4GHz'
    }

    def __init__(self, is5_g_hz=None, is5_g_hz_u=None, is5_g_hz_l=None, is2dot4_g_hz=None):  # noqa: E501
        """MinMaxAvgValueIntPerRadioMap - a model defined in Swagger"""  # noqa: E501
        self._is5_g_hz = None
        self._is5_g_hz_u = None
        self._is5_g_hz_l = None
        self._is2dot4_g_hz = None
        self.discriminator = None
        if is5_g_hz is not None:
            self.is5_g_hz = is5_g_hz
        if is5_g_hz_u is not None:
            self.is5_g_hz_u = is5_g_hz_u
        if is5_g_hz_l is not None:
            self.is5_g_hz_l = is5_g_hz_l
        if is2dot4_g_hz is not None:
            self.is2dot4_g_hz = is2dot4_g_hz

    @property
    def is5_g_hz(self):
        """Gets the is5_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501


        :return: The is5_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._is5_g_hz

    @is5_g_hz.setter
    def is5_g_hz(self, is5_g_hz):
        """Sets the is5_g_hz of this MinMaxAvgValueIntPerRadioMap.


        :param is5_g_hz: The is5_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._is5_g_hz = is5_g_hz

    @property
    def is5_g_hz_u(self):
        """Gets the is5_g_hz_u of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501


        :return: The is5_g_hz_u of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._is5_g_hz_u

    @is5_g_hz_u.setter
    def is5_g_hz_u(self, is5_g_hz_u):
        """Sets the is5_g_hz_u of this MinMaxAvgValueIntPerRadioMap.


        :param is5_g_hz_u: The is5_g_hz_u of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._is5_g_hz_u = is5_g_hz_u

    @property
    def is5_g_hz_l(self):
        """Gets the is5_g_hz_l of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501


        :return: The is5_g_hz_l of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._is5_g_hz_l

    @is5_g_hz_l.setter
    def is5_g_hz_l(self, is5_g_hz_l):
        """Sets the is5_g_hz_l of this MinMaxAvgValueIntPerRadioMap.


        :param is5_g_hz_l: The is5_g_hz_l of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._is5_g_hz_l = is5_g_hz_l

    @property
    def is2dot4_g_hz(self):
        """Gets the is2dot4_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501


        :return: The is2dot4_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :rtype: MinMaxAvgValueInt
        """
        return self._is2dot4_g_hz

    @is2dot4_g_hz.setter
    def is2dot4_g_hz(self, is2dot4_g_hz):
        """Sets the is2dot4_g_hz of this MinMaxAvgValueIntPerRadioMap.


        :param is2dot4_g_hz: The is2dot4_g_hz of this MinMaxAvgValueIntPerRadioMap.  # noqa: E501
        :type: MinMaxAvgValueInt
        """

        self._is2dot4_g_hz = is2dot4_g_hz

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
        if issubclass(MinMaxAvgValueIntPerRadioMap, dict):
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
        if not isinstance(other, MinMaxAvgValueIntPerRadioMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
