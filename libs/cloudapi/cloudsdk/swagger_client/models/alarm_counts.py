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

class AlarmCounts(object):
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
        'counts_per_equipment_id_map': 'CountsPerEquipmentIdPerAlarmCodeMap',
        'total_counts_per_alarm_code_map': 'CountsPerAlarmCodeMap'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'counts_per_equipment_id_map': 'countsPerEquipmentIdMap',
        'total_counts_per_alarm_code_map': 'totalCountsPerAlarmCodeMap'
    }

    def __init__(self, customer_id=None, counts_per_equipment_id_map=None, total_counts_per_alarm_code_map=None):  # noqa: E501
        """AlarmCounts - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._counts_per_equipment_id_map = None
        self._total_counts_per_alarm_code_map = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if counts_per_equipment_id_map is not None:
            self.counts_per_equipment_id_map = counts_per_equipment_id_map
        if total_counts_per_alarm_code_map is not None:
            self.total_counts_per_alarm_code_map = total_counts_per_alarm_code_map

    @property
    def customer_id(self):
        """Gets the customer_id of this AlarmCounts.  # noqa: E501


        :return: The customer_id of this AlarmCounts.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AlarmCounts.


        :param customer_id: The customer_id of this AlarmCounts.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def counts_per_equipment_id_map(self):
        """Gets the counts_per_equipment_id_map of this AlarmCounts.  # noqa: E501


        :return: The counts_per_equipment_id_map of this AlarmCounts.  # noqa: E501
        :rtype: CountsPerEquipmentIdPerAlarmCodeMap
        """
        return self._counts_per_equipment_id_map

    @counts_per_equipment_id_map.setter
    def counts_per_equipment_id_map(self, counts_per_equipment_id_map):
        """Sets the counts_per_equipment_id_map of this AlarmCounts.


        :param counts_per_equipment_id_map: The counts_per_equipment_id_map of this AlarmCounts.  # noqa: E501
        :type: CountsPerEquipmentIdPerAlarmCodeMap
        """

        self._counts_per_equipment_id_map = counts_per_equipment_id_map

    @property
    def total_counts_per_alarm_code_map(self):
        """Gets the total_counts_per_alarm_code_map of this AlarmCounts.  # noqa: E501


        :return: The total_counts_per_alarm_code_map of this AlarmCounts.  # noqa: E501
        :rtype: CountsPerAlarmCodeMap
        """
        return self._total_counts_per_alarm_code_map

    @total_counts_per_alarm_code_map.setter
    def total_counts_per_alarm_code_map(self, total_counts_per_alarm_code_map):
        """Sets the total_counts_per_alarm_code_map of this AlarmCounts.


        :param total_counts_per_alarm_code_map: The total_counts_per_alarm_code_map of this AlarmCounts.  # noqa: E501
        :type: CountsPerAlarmCodeMap
        """

        self._total_counts_per_alarm_code_map = total_counts_per_alarm_code_map

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
        if issubclass(AlarmCounts, dict):
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
        if not isinstance(other, AlarmCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
