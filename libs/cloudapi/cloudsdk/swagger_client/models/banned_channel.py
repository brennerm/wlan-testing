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

class BannedChannel(object):
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
        'channel_number': 'int',
        'banned_on_epoc': 'int'
    }

    attribute_map = {
        'channel_number': 'channelNumber',
        'banned_on_epoc': 'bannedOnEpoc'
    }

    def __init__(self, channel_number=None, banned_on_epoc=None):  # noqa: E501
        """BannedChannel - a model defined in Swagger"""  # noqa: E501
        self._channel_number = None
        self._banned_on_epoc = None
        self.discriminator = None
        if channel_number is not None:
            self.channel_number = channel_number
        if banned_on_epoc is not None:
            self.banned_on_epoc = banned_on_epoc

    @property
    def channel_number(self):
        """Gets the channel_number of this BannedChannel.  # noqa: E501


        :return: The channel_number of this BannedChannel.  # noqa: E501
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this BannedChannel.


        :param channel_number: The channel_number of this BannedChannel.  # noqa: E501
        :type: int
        """

        self._channel_number = channel_number

    @property
    def banned_on_epoc(self):
        """Gets the banned_on_epoc of this BannedChannel.  # noqa: E501


        :return: The banned_on_epoc of this BannedChannel.  # noqa: E501
        :rtype: int
        """
        return self._banned_on_epoc

    @banned_on_epoc.setter
    def banned_on_epoc(self, banned_on_epoc):
        """Sets the banned_on_epoc of this BannedChannel.


        :param banned_on_epoc: The banned_on_epoc of this BannedChannel.  # noqa: E501
        :type: int
        """

        self._banned_on_epoc = banned_on_epoc

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
        if issubclass(BannedChannel, dict):
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
        if not isinstance(other, BannedChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
