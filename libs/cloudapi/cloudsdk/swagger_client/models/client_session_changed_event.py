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

class ClientSessionChangedEvent(object):
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
        'event_timestamp': 'int',
        'customer_id': 'int',
        'equipment_id': 'int',
        'payload': 'ClientSession'
    }

    attribute_map = {
        'model_type': 'model_type',
        'event_timestamp': 'eventTimestamp',
        'customer_id': 'customerId',
        'equipment_id': 'equipmentId',
        'payload': 'payload'
    }

    def __init__(self, model_type=None, event_timestamp=None, customer_id=None, equipment_id=None, payload=None):  # noqa: E501
        """ClientSessionChangedEvent - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._event_timestamp = None
        self._customer_id = None
        self._equipment_id = None
        self._payload = None
        self.discriminator = None
        self.model_type = model_type
        if event_timestamp is not None:
            self.event_timestamp = event_timestamp
        if customer_id is not None:
            self.customer_id = customer_id
        if equipment_id is not None:
            self.equipment_id = equipment_id
        if payload is not None:
            self.payload = payload

    @property
    def model_type(self):
        """Gets the model_type of this ClientSessionChangedEvent.  # noqa: E501


        :return: The model_type of this ClientSessionChangedEvent.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ClientSessionChangedEvent.


        :param model_type: The model_type of this ClientSessionChangedEvent.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def event_timestamp(self):
        """Gets the event_timestamp of this ClientSessionChangedEvent.  # noqa: E501


        :return: The event_timestamp of this ClientSessionChangedEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_timestamp

    @event_timestamp.setter
    def event_timestamp(self, event_timestamp):
        """Sets the event_timestamp of this ClientSessionChangedEvent.


        :param event_timestamp: The event_timestamp of this ClientSessionChangedEvent.  # noqa: E501
        :type: int
        """

        self._event_timestamp = event_timestamp

    @property
    def customer_id(self):
        """Gets the customer_id of this ClientSessionChangedEvent.  # noqa: E501


        :return: The customer_id of this ClientSessionChangedEvent.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ClientSessionChangedEvent.


        :param customer_id: The customer_id of this ClientSessionChangedEvent.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def equipment_id(self):
        """Gets the equipment_id of this ClientSessionChangedEvent.  # noqa: E501


        :return: The equipment_id of this ClientSessionChangedEvent.  # noqa: E501
        :rtype: int
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        """Sets the equipment_id of this ClientSessionChangedEvent.


        :param equipment_id: The equipment_id of this ClientSessionChangedEvent.  # noqa: E501
        :type: int
        """

        self._equipment_id = equipment_id

    @property
    def payload(self):
        """Gets the payload of this ClientSessionChangedEvent.  # noqa: E501


        :return: The payload of this ClientSessionChangedEvent.  # noqa: E501
        :rtype: ClientSession
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ClientSessionChangedEvent.


        :param payload: The payload of this ClientSessionChangedEvent.  # noqa: E501
        :type: ClientSession
        """

        self._payload = payload

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
        if issubclass(ClientSessionChangedEvent, dict):
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
        if not isinstance(other, ClientSessionChangedEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
