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

class PasspointVenueName(object):
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
        'venue_url': 'str'
    }

    attribute_map = {
        'venue_url': 'venueUrl'
    }

    def __init__(self, venue_url=None):  # noqa: E501
        """PasspointVenueName - a model defined in Swagger"""  # noqa: E501
        self._venue_url = None
        self.discriminator = None
        if venue_url is not None:
            self.venue_url = venue_url

    @property
    def venue_url(self):
        """Gets the venue_url of this PasspointVenueName.  # noqa: E501


        :return: The venue_url of this PasspointVenueName.  # noqa: E501
        :rtype: str
        """
        return self._venue_url

    @venue_url.setter
    def venue_url(self, venue_url):
        """Sets the venue_url of this PasspointVenueName.


        :param venue_url: The venue_url of this PasspointVenueName.  # noqa: E501
        :type: str
        """

        self._venue_url = venue_url

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
        if issubclass(PasspointVenueName, dict):
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
        if not isinstance(other, PasspointVenueName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
