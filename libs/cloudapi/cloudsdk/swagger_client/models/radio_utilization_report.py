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

class RadioUtilizationReport(object):
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
        'status_data_type': 'str',
        'radio_utilization': 'EquipmentPerRadioUtilizationDetailsMap',
        'capacity_details': 'EquipmentCapacityDetailsMap',
        'avg_noise_floor': 'IntegerPerRadioTypeMap'
    }

    attribute_map = {
        'model_type': 'model_type',
        'status_data_type': 'statusDataType',
        'radio_utilization': 'radioUtilization',
        'capacity_details': 'capacityDetails',
        'avg_noise_floor': 'avgNoiseFloor'
    }

    def __init__(self, model_type=None, status_data_type=None, radio_utilization=None, capacity_details=None, avg_noise_floor=None):  # noqa: E501
        """RadioUtilizationReport - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._status_data_type = None
        self._radio_utilization = None
        self._capacity_details = None
        self._avg_noise_floor = None
        self.discriminator = None
        self.model_type = model_type
        if status_data_type is not None:
            self.status_data_type = status_data_type
        if radio_utilization is not None:
            self.radio_utilization = radio_utilization
        if capacity_details is not None:
            self.capacity_details = capacity_details
        if avg_noise_floor is not None:
            self.avg_noise_floor = avg_noise_floor

    @property
    def model_type(self):
        """Gets the model_type of this RadioUtilizationReport.  # noqa: E501


        :return: The model_type of this RadioUtilizationReport.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this RadioUtilizationReport.


        :param model_type: The model_type of this RadioUtilizationReport.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501
        allowed_values = ["RadioUtilizationReport"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def status_data_type(self):
        """Gets the status_data_type of this RadioUtilizationReport.  # noqa: E501


        :return: The status_data_type of this RadioUtilizationReport.  # noqa: E501
        :rtype: str
        """
        return self._status_data_type

    @status_data_type.setter
    def status_data_type(self, status_data_type):
        """Sets the status_data_type of this RadioUtilizationReport.


        :param status_data_type: The status_data_type of this RadioUtilizationReport.  # noqa: E501
        :type: str
        """
        allowed_values = ["RADIO_UTILIZATION"]  # noqa: E501
        if status_data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `status_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(status_data_type, allowed_values)
            )

        self._status_data_type = status_data_type

    @property
    def radio_utilization(self):
        """Gets the radio_utilization of this RadioUtilizationReport.  # noqa: E501


        :return: The radio_utilization of this RadioUtilizationReport.  # noqa: E501
        :rtype: EquipmentPerRadioUtilizationDetailsMap
        """
        return self._radio_utilization

    @radio_utilization.setter
    def radio_utilization(self, radio_utilization):
        """Sets the radio_utilization of this RadioUtilizationReport.


        :param radio_utilization: The radio_utilization of this RadioUtilizationReport.  # noqa: E501
        :type: EquipmentPerRadioUtilizationDetailsMap
        """

        self._radio_utilization = radio_utilization

    @property
    def capacity_details(self):
        """Gets the capacity_details of this RadioUtilizationReport.  # noqa: E501


        :return: The capacity_details of this RadioUtilizationReport.  # noqa: E501
        :rtype: EquipmentCapacityDetailsMap
        """
        return self._capacity_details

    @capacity_details.setter
    def capacity_details(self, capacity_details):
        """Sets the capacity_details of this RadioUtilizationReport.


        :param capacity_details: The capacity_details of this RadioUtilizationReport.  # noqa: E501
        :type: EquipmentCapacityDetailsMap
        """

        self._capacity_details = capacity_details

    @property
    def avg_noise_floor(self):
        """Gets the avg_noise_floor of this RadioUtilizationReport.  # noqa: E501


        :return: The avg_noise_floor of this RadioUtilizationReport.  # noqa: E501
        :rtype: IntegerPerRadioTypeMap
        """
        return self._avg_noise_floor

    @avg_noise_floor.setter
    def avg_noise_floor(self, avg_noise_floor):
        """Sets the avg_noise_floor of this RadioUtilizationReport.


        :param avg_noise_floor: The avg_noise_floor of this RadioUtilizationReport.  # noqa: E501
        :type: IntegerPerRadioTypeMap
        """

        self._avg_noise_floor = avg_noise_floor

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
        if issubclass(RadioUtilizationReport, dict):
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
        if not isinstance(other, RadioUtilizationReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
