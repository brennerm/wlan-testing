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

class PaginationContextLocation(object):
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
        'max_items_per_page': 'int',
        'last_returned_page_number': 'int',
        'total_items_returned': 'int',
        'last_page': 'bool',
        'cursor': 'str'
    }

    attribute_map = {
        'model_type': 'model_type',
        'max_items_per_page': 'maxItemsPerPage',
        'last_returned_page_number': 'lastReturnedPageNumber',
        'total_items_returned': 'totalItemsReturned',
        'last_page': 'lastPage',
        'cursor': 'cursor'
    }

    def __init__(self, model_type=None, max_items_per_page=20, last_returned_page_number=None, total_items_returned=None, last_page=None, cursor=None):  # noqa: E501
        """PaginationContextLocation - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._max_items_per_page = None
        self._last_returned_page_number = None
        self._total_items_returned = None
        self._last_page = None
        self._cursor = None
        self.discriminator = None
        if model_type is not None:
            self.model_type = model_type
        self.max_items_per_page = max_items_per_page
        if last_returned_page_number is not None:
            self.last_returned_page_number = last_returned_page_number
        if total_items_returned is not None:
            self.total_items_returned = total_items_returned
        if last_page is not None:
            self.last_page = last_page
        if cursor is not None:
            self.cursor = cursor

    @property
    def model_type(self):
        """Gets the model_type of this PaginationContextLocation.  # noqa: E501


        :return: The model_type of this PaginationContextLocation.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this PaginationContextLocation.


        :param model_type: The model_type of this PaginationContextLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["PaginationContext"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def max_items_per_page(self):
        """Gets the max_items_per_page of this PaginationContextLocation.  # noqa: E501


        :return: The max_items_per_page of this PaginationContextLocation.  # noqa: E501
        :rtype: int
        """
        return self._max_items_per_page

    @max_items_per_page.setter
    def max_items_per_page(self, max_items_per_page):
        """Sets the max_items_per_page of this PaginationContextLocation.


        :param max_items_per_page: The max_items_per_page of this PaginationContextLocation.  # noqa: E501
        :type: int
        """
        if max_items_per_page is None:
            raise ValueError("Invalid value for `max_items_per_page`, must not be `None`")  # noqa: E501

        self._max_items_per_page = max_items_per_page

    @property
    def last_returned_page_number(self):
        """Gets the last_returned_page_number of this PaginationContextLocation.  # noqa: E501


        :return: The last_returned_page_number of this PaginationContextLocation.  # noqa: E501
        :rtype: int
        """
        return self._last_returned_page_number

    @last_returned_page_number.setter
    def last_returned_page_number(self, last_returned_page_number):
        """Sets the last_returned_page_number of this PaginationContextLocation.


        :param last_returned_page_number: The last_returned_page_number of this PaginationContextLocation.  # noqa: E501
        :type: int
        """

        self._last_returned_page_number = last_returned_page_number

    @property
    def total_items_returned(self):
        """Gets the total_items_returned of this PaginationContextLocation.  # noqa: E501


        :return: The total_items_returned of this PaginationContextLocation.  # noqa: E501
        :rtype: int
        """
        return self._total_items_returned

    @total_items_returned.setter
    def total_items_returned(self, total_items_returned):
        """Sets the total_items_returned of this PaginationContextLocation.


        :param total_items_returned: The total_items_returned of this PaginationContextLocation.  # noqa: E501
        :type: int
        """

        self._total_items_returned = total_items_returned

    @property
    def last_page(self):
        """Gets the last_page of this PaginationContextLocation.  # noqa: E501


        :return: The last_page of this PaginationContextLocation.  # noqa: E501
        :rtype: bool
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this PaginationContextLocation.


        :param last_page: The last_page of this PaginationContextLocation.  # noqa: E501
        :type: bool
        """

        self._last_page = last_page

    @property
    def cursor(self):
        """Gets the cursor of this PaginationContextLocation.  # noqa: E501


        :return: The cursor of this PaginationContextLocation.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this PaginationContextLocation.


        :param cursor: The cursor of this PaginationContextLocation.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

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
        if issubclass(PaginationContextLocation, dict):
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
        if not isinstance(other, PaginationContextLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
