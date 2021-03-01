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

class CustomerFirmwareTrackRecord(object):
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
        'customer_id': 'int',
        'track_record_id': 'int',
        'settings': 'CustomerFirmwareTrackSettings',
        'created_timestamp': 'int',
        'last_modified_timestamp': 'int'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'track_record_id': 'trackRecordId',
        'settings': 'settings',
        'created_timestamp': 'createdTimestamp',
        'last_modified_timestamp': 'lastModifiedTimestamp'
    }

    def __init__(self, customer_id=None, track_record_id=None, settings=None, created_timestamp=None, last_modified_timestamp=None):  # noqa: E501
        """CustomerFirmwareTrackRecord - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._track_record_id = None
        self._settings = None
        self._created_timestamp = None
        self._last_modified_timestamp = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if track_record_id is not None:
            self.track_record_id = track_record_id
        if settings is not None:
            self.settings = settings
        if created_timestamp is not None:
            self.created_timestamp = created_timestamp
        if last_modified_timestamp is not None:
            self.last_modified_timestamp = last_modified_timestamp

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerFirmwareTrackRecord.  # noqa: E501


        :return: The customer_id of this CustomerFirmwareTrackRecord.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerFirmwareTrackRecord.


        :param customer_id: The customer_id of this CustomerFirmwareTrackRecord.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def track_record_id(self):
        """Gets the track_record_id of this CustomerFirmwareTrackRecord.  # noqa: E501


        :return: The track_record_id of this CustomerFirmwareTrackRecord.  # noqa: E501
        :rtype: int
        """
        return self._track_record_id

    @track_record_id.setter
    def track_record_id(self, track_record_id):
        """Sets the track_record_id of this CustomerFirmwareTrackRecord.


        :param track_record_id: The track_record_id of this CustomerFirmwareTrackRecord.  # noqa: E501
        :type: int
        """

        self._track_record_id = track_record_id

    @property
    def settings(self):
        """Gets the settings of this CustomerFirmwareTrackRecord.  # noqa: E501


        :return: The settings of this CustomerFirmwareTrackRecord.  # noqa: E501
        :rtype: CustomerFirmwareTrackSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this CustomerFirmwareTrackRecord.


        :param settings: The settings of this CustomerFirmwareTrackRecord.  # noqa: E501
        :type: CustomerFirmwareTrackSettings
        """

        self._settings = settings

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501


        :return: The created_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501
        :rtype: int
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this CustomerFirmwareTrackRecord.


        :param created_timestamp: The created_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501
        :type: int
        """

        self._created_timestamp = created_timestamp

    @property
    def last_modified_timestamp(self):
        """Gets the last_modified_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501

        must be provided for update operation, update will be rejected if provided value does not match the one currently stored in the database  # noqa: E501

        :return: The last_modified_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        """Sets the last_modified_timestamp of this CustomerFirmwareTrackRecord.

        must be provided for update operation, update will be rejected if provided value does not match the one currently stored in the database  # noqa: E501

        :param last_modified_timestamp: The last_modified_timestamp of this CustomerFirmwareTrackRecord.  # noqa: E501
        :type: int
        """

        self._last_modified_timestamp = last_modified_timestamp

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
        if issubclass(CustomerFirmwareTrackRecord, dict):
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
        if not isinstance(other, CustomerFirmwareTrackRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
