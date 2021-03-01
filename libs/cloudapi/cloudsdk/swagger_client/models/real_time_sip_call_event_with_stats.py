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

class RealTimeSipCallEventWithStats(object):
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
        'all_of': 'RealTimeEvent',
        'sip_call_id': 'int',
        'association_id': 'int',
        'client_mac_address': 'MacAddress',
        'radio_type': 'RadioType',
        'statuses': 'list[RtpFlowStats]',
        'channel': 'int',
        'codecs': 'list[str]',
        'provider_domain': 'str'
    }

    attribute_map = {
        'model_type': 'model_type',
        'all_of': 'allOf',
        'sip_call_id': 'sipCallId',
        'association_id': 'associationId',
        'client_mac_address': 'clientMacAddress',
        'radio_type': 'radioType',
        'statuses': 'statuses',
        'channel': 'channel',
        'codecs': 'codecs',
        'provider_domain': 'providerDomain'
    }

    def __init__(self, model_type=None, all_of=None, sip_call_id=None, association_id=None, client_mac_address=None, radio_type=None, statuses=None, channel=None, codecs=None, provider_domain=None):  # noqa: E501
        """RealTimeSipCallEventWithStats - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._all_of = None
        self._sip_call_id = None
        self._association_id = None
        self._client_mac_address = None
        self._radio_type = None
        self._statuses = None
        self._channel = None
        self._codecs = None
        self._provider_domain = None
        self.discriminator = None
        self.model_type = model_type
        if all_of is not None:
            self.all_of = all_of
        if sip_call_id is not None:
            self.sip_call_id = sip_call_id
        if association_id is not None:
            self.association_id = association_id
        if client_mac_address is not None:
            self.client_mac_address = client_mac_address
        if radio_type is not None:
            self.radio_type = radio_type
        if statuses is not None:
            self.statuses = statuses
        if channel is not None:
            self.channel = channel
        if codecs is not None:
            self.codecs = codecs
        if provider_domain is not None:
            self.provider_domain = provider_domain

    @property
    def model_type(self):
        """Gets the model_type of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The model_type of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this RealTimeSipCallEventWithStats.


        :param model_type: The model_type of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def all_of(self):
        """Gets the all_of of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The all_of of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: RealTimeEvent
        """
        return self._all_of

    @all_of.setter
    def all_of(self, all_of):
        """Sets the all_of of this RealTimeSipCallEventWithStats.


        :param all_of: The all_of of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: RealTimeEvent
        """

        self._all_of = all_of

    @property
    def sip_call_id(self):
        """Gets the sip_call_id of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The sip_call_id of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: int
        """
        return self._sip_call_id

    @sip_call_id.setter
    def sip_call_id(self, sip_call_id):
        """Sets the sip_call_id of this RealTimeSipCallEventWithStats.


        :param sip_call_id: The sip_call_id of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: int
        """

        self._sip_call_id = sip_call_id

    @property
    def association_id(self):
        """Gets the association_id of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The association_id of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: int
        """
        return self._association_id

    @association_id.setter
    def association_id(self, association_id):
        """Sets the association_id of this RealTimeSipCallEventWithStats.


        :param association_id: The association_id of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: int
        """

        self._association_id = association_id

    @property
    def client_mac_address(self):
        """Gets the client_mac_address of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The client_mac_address of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: MacAddress
        """
        return self._client_mac_address

    @client_mac_address.setter
    def client_mac_address(self, client_mac_address):
        """Sets the client_mac_address of this RealTimeSipCallEventWithStats.


        :param client_mac_address: The client_mac_address of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: MacAddress
        """

        self._client_mac_address = client_mac_address

    @property
    def radio_type(self):
        """Gets the radio_type of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The radio_type of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: RadioType
        """
        return self._radio_type

    @radio_type.setter
    def radio_type(self, radio_type):
        """Sets the radio_type of this RealTimeSipCallEventWithStats.


        :param radio_type: The radio_type of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: RadioType
        """

        self._radio_type = radio_type

    @property
    def statuses(self):
        """Gets the statuses of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The statuses of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: list[RtpFlowStats]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this RealTimeSipCallEventWithStats.


        :param statuses: The statuses of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: list[RtpFlowStats]
        """

        self._statuses = statuses

    @property
    def channel(self):
        """Gets the channel of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The channel of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this RealTimeSipCallEventWithStats.


        :param channel: The channel of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def codecs(self):
        """Gets the codecs of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The codecs of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: list[str]
        """
        return self._codecs

    @codecs.setter
    def codecs(self, codecs):
        """Sets the codecs of this RealTimeSipCallEventWithStats.


        :param codecs: The codecs of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: list[str]
        """

        self._codecs = codecs

    @property
    def provider_domain(self):
        """Gets the provider_domain of this RealTimeSipCallEventWithStats.  # noqa: E501


        :return: The provider_domain of this RealTimeSipCallEventWithStats.  # noqa: E501
        :rtype: str
        """
        return self._provider_domain

    @provider_domain.setter
    def provider_domain(self, provider_domain):
        """Sets the provider_domain of this RealTimeSipCallEventWithStats.


        :param provider_domain: The provider_domain of this RealTimeSipCallEventWithStats.  # noqa: E501
        :type: str
        """

        self._provider_domain = provider_domain

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
        if issubclass(RealTimeSipCallEventWithStats, dict):
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
        if not isinstance(other, RealTimeSipCallEventWithStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
