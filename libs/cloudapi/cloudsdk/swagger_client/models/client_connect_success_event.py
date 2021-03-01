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

class ClientConnectSuccessEvent(object):
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
        'client_mac_address': 'MacAddress',
        'session_id': 'int',
        'radio_type': 'RadioType',
        'is_reassociation': 'bool',
        'ssid': 'str',
        'security_type': 'SecurityType',
        'fbt_used': 'bool',
        'ip_addr': 'str',
        'clt_id': 'str',
        'auth_ts': 'int',
        'assoc_ts': 'int',
        'eapol_ts': 'int',
        'port_enabled_ts': 'int',
        'first_data_rx_ts': 'int',
        'first_data_tx_ts': 'int',
        'using11k': 'bool',
        'using11r': 'bool',
        'using11v': 'bool',
        'ip_acquisition_ts': 'int',
        'assoc_rssi': 'int'
    }

    attribute_map = {
        'model_type': 'model_type',
        'all_of': 'allOf',
        'client_mac_address': 'clientMacAddress',
        'session_id': 'sessionId',
        'radio_type': 'radioType',
        'is_reassociation': 'isReassociation',
        'ssid': 'ssid',
        'security_type': 'securityType',
        'fbt_used': 'fbtUsed',
        'ip_addr': 'ipAddr',
        'clt_id': 'cltId',
        'auth_ts': 'authTs',
        'assoc_ts': 'assocTs',
        'eapol_ts': 'eapolTs',
        'port_enabled_ts': 'portEnabledTs',
        'first_data_rx_ts': 'firstDataRxTs',
        'first_data_tx_ts': 'firstDataTxTs',
        'using11k': 'using11k',
        'using11r': 'using11r',
        'using11v': 'using11v',
        'ip_acquisition_ts': 'ipAcquisitionTs',
        'assoc_rssi': 'assocRssi'
    }

    def __init__(self, model_type=None, all_of=None, client_mac_address=None, session_id=None, radio_type=None, is_reassociation=None, ssid=None, security_type=None, fbt_used=None, ip_addr=None, clt_id=None, auth_ts=None, assoc_ts=None, eapol_ts=None, port_enabled_ts=None, first_data_rx_ts=None, first_data_tx_ts=None, using11k=None, using11r=None, using11v=None, ip_acquisition_ts=None, assoc_rssi=None):  # noqa: E501
        """ClientConnectSuccessEvent - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._all_of = None
        self._client_mac_address = None
        self._session_id = None
        self._radio_type = None
        self._is_reassociation = None
        self._ssid = None
        self._security_type = None
        self._fbt_used = None
        self._ip_addr = None
        self._clt_id = None
        self._auth_ts = None
        self._assoc_ts = None
        self._eapol_ts = None
        self._port_enabled_ts = None
        self._first_data_rx_ts = None
        self._first_data_tx_ts = None
        self._using11k = None
        self._using11r = None
        self._using11v = None
        self._ip_acquisition_ts = None
        self._assoc_rssi = None
        self.discriminator = None
        self.model_type = model_type
        if all_of is not None:
            self.all_of = all_of
        if client_mac_address is not None:
            self.client_mac_address = client_mac_address
        if session_id is not None:
            self.session_id = session_id
        if radio_type is not None:
            self.radio_type = radio_type
        if is_reassociation is not None:
            self.is_reassociation = is_reassociation
        if ssid is not None:
            self.ssid = ssid
        if security_type is not None:
            self.security_type = security_type
        if fbt_used is not None:
            self.fbt_used = fbt_used
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if clt_id is not None:
            self.clt_id = clt_id
        if auth_ts is not None:
            self.auth_ts = auth_ts
        if assoc_ts is not None:
            self.assoc_ts = assoc_ts
        if eapol_ts is not None:
            self.eapol_ts = eapol_ts
        if port_enabled_ts is not None:
            self.port_enabled_ts = port_enabled_ts
        if first_data_rx_ts is not None:
            self.first_data_rx_ts = first_data_rx_ts
        if first_data_tx_ts is not None:
            self.first_data_tx_ts = first_data_tx_ts
        if using11k is not None:
            self.using11k = using11k
        if using11r is not None:
            self.using11r = using11r
        if using11v is not None:
            self.using11v = using11v
        if ip_acquisition_ts is not None:
            self.ip_acquisition_ts = ip_acquisition_ts
        if assoc_rssi is not None:
            self.assoc_rssi = assoc_rssi

    @property
    def model_type(self):
        """Gets the model_type of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The model_type of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ClientConnectSuccessEvent.


        :param model_type: The model_type of this ClientConnectSuccessEvent.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def all_of(self):
        """Gets the all_of of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The all_of of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: RealTimeEvent
        """
        return self._all_of

    @all_of.setter
    def all_of(self, all_of):
        """Sets the all_of of this ClientConnectSuccessEvent.


        :param all_of: The all_of of this ClientConnectSuccessEvent.  # noqa: E501
        :type: RealTimeEvent
        """

        self._all_of = all_of

    @property
    def client_mac_address(self):
        """Gets the client_mac_address of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The client_mac_address of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: MacAddress
        """
        return self._client_mac_address

    @client_mac_address.setter
    def client_mac_address(self, client_mac_address):
        """Sets the client_mac_address of this ClientConnectSuccessEvent.


        :param client_mac_address: The client_mac_address of this ClientConnectSuccessEvent.  # noqa: E501
        :type: MacAddress
        """

        self._client_mac_address = client_mac_address

    @property
    def session_id(self):
        """Gets the session_id of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The session_id of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ClientConnectSuccessEvent.


        :param session_id: The session_id of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._session_id = session_id

    @property
    def radio_type(self):
        """Gets the radio_type of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The radio_type of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: RadioType
        """
        return self._radio_type

    @radio_type.setter
    def radio_type(self, radio_type):
        """Sets the radio_type of this ClientConnectSuccessEvent.


        :param radio_type: The radio_type of this ClientConnectSuccessEvent.  # noqa: E501
        :type: RadioType
        """

        self._radio_type = radio_type

    @property
    def is_reassociation(self):
        """Gets the is_reassociation of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The is_reassociation of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_reassociation

    @is_reassociation.setter
    def is_reassociation(self, is_reassociation):
        """Sets the is_reassociation of this ClientConnectSuccessEvent.


        :param is_reassociation: The is_reassociation of this ClientConnectSuccessEvent.  # noqa: E501
        :type: bool
        """

        self._is_reassociation = is_reassociation

    @property
    def ssid(self):
        """Gets the ssid of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The ssid of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this ClientConnectSuccessEvent.


        :param ssid: The ssid of this ClientConnectSuccessEvent.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def security_type(self):
        """Gets the security_type of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The security_type of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: SecurityType
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this ClientConnectSuccessEvent.


        :param security_type: The security_type of this ClientConnectSuccessEvent.  # noqa: E501
        :type: SecurityType
        """

        self._security_type = security_type

    @property
    def fbt_used(self):
        """Gets the fbt_used of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The fbt_used of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: bool
        """
        return self._fbt_used

    @fbt_used.setter
    def fbt_used(self, fbt_used):
        """Sets the fbt_used of this ClientConnectSuccessEvent.


        :param fbt_used: The fbt_used of this ClientConnectSuccessEvent.  # noqa: E501
        :type: bool
        """

        self._fbt_used = fbt_used

    @property
    def ip_addr(self):
        """Gets the ip_addr of this ClientConnectSuccessEvent.  # noqa: E501

        string representing InetAddress  # noqa: E501

        :return: The ip_addr of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this ClientConnectSuccessEvent.

        string representing InetAddress  # noqa: E501

        :param ip_addr: The ip_addr of this ClientConnectSuccessEvent.  # noqa: E501
        :type: str
        """

        self._ip_addr = ip_addr

    @property
    def clt_id(self):
        """Gets the clt_id of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The clt_id of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: str
        """
        return self._clt_id

    @clt_id.setter
    def clt_id(self, clt_id):
        """Sets the clt_id of this ClientConnectSuccessEvent.


        :param clt_id: The clt_id of this ClientConnectSuccessEvent.  # noqa: E501
        :type: str
        """

        self._clt_id = clt_id

    @property
    def auth_ts(self):
        """Gets the auth_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The auth_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._auth_ts

    @auth_ts.setter
    def auth_ts(self, auth_ts):
        """Sets the auth_ts of this ClientConnectSuccessEvent.


        :param auth_ts: The auth_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._auth_ts = auth_ts

    @property
    def assoc_ts(self):
        """Gets the assoc_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The assoc_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._assoc_ts

    @assoc_ts.setter
    def assoc_ts(self, assoc_ts):
        """Sets the assoc_ts of this ClientConnectSuccessEvent.


        :param assoc_ts: The assoc_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._assoc_ts = assoc_ts

    @property
    def eapol_ts(self):
        """Gets the eapol_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The eapol_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._eapol_ts

    @eapol_ts.setter
    def eapol_ts(self, eapol_ts):
        """Sets the eapol_ts of this ClientConnectSuccessEvent.


        :param eapol_ts: The eapol_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._eapol_ts = eapol_ts

    @property
    def port_enabled_ts(self):
        """Gets the port_enabled_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The port_enabled_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._port_enabled_ts

    @port_enabled_ts.setter
    def port_enabled_ts(self, port_enabled_ts):
        """Sets the port_enabled_ts of this ClientConnectSuccessEvent.


        :param port_enabled_ts: The port_enabled_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._port_enabled_ts = port_enabled_ts

    @property
    def first_data_rx_ts(self):
        """Gets the first_data_rx_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The first_data_rx_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._first_data_rx_ts

    @first_data_rx_ts.setter
    def first_data_rx_ts(self, first_data_rx_ts):
        """Sets the first_data_rx_ts of this ClientConnectSuccessEvent.


        :param first_data_rx_ts: The first_data_rx_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._first_data_rx_ts = first_data_rx_ts

    @property
    def first_data_tx_ts(self):
        """Gets the first_data_tx_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The first_data_tx_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._first_data_tx_ts

    @first_data_tx_ts.setter
    def first_data_tx_ts(self, first_data_tx_ts):
        """Sets the first_data_tx_ts of this ClientConnectSuccessEvent.


        :param first_data_tx_ts: The first_data_tx_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._first_data_tx_ts = first_data_tx_ts

    @property
    def using11k(self):
        """Gets the using11k of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The using11k of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: bool
        """
        return self._using11k

    @using11k.setter
    def using11k(self, using11k):
        """Sets the using11k of this ClientConnectSuccessEvent.


        :param using11k: The using11k of this ClientConnectSuccessEvent.  # noqa: E501
        :type: bool
        """

        self._using11k = using11k

    @property
    def using11r(self):
        """Gets the using11r of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The using11r of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: bool
        """
        return self._using11r

    @using11r.setter
    def using11r(self, using11r):
        """Sets the using11r of this ClientConnectSuccessEvent.


        :param using11r: The using11r of this ClientConnectSuccessEvent.  # noqa: E501
        :type: bool
        """

        self._using11r = using11r

    @property
    def using11v(self):
        """Gets the using11v of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The using11v of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: bool
        """
        return self._using11v

    @using11v.setter
    def using11v(self, using11v):
        """Sets the using11v of this ClientConnectSuccessEvent.


        :param using11v: The using11v of this ClientConnectSuccessEvent.  # noqa: E501
        :type: bool
        """

        self._using11v = using11v

    @property
    def ip_acquisition_ts(self):
        """Gets the ip_acquisition_ts of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The ip_acquisition_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._ip_acquisition_ts

    @ip_acquisition_ts.setter
    def ip_acquisition_ts(self, ip_acquisition_ts):
        """Sets the ip_acquisition_ts of this ClientConnectSuccessEvent.


        :param ip_acquisition_ts: The ip_acquisition_ts of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._ip_acquisition_ts = ip_acquisition_ts

    @property
    def assoc_rssi(self):
        """Gets the assoc_rssi of this ClientConnectSuccessEvent.  # noqa: E501


        :return: The assoc_rssi of this ClientConnectSuccessEvent.  # noqa: E501
        :rtype: int
        """
        return self._assoc_rssi

    @assoc_rssi.setter
    def assoc_rssi(self, assoc_rssi):
        """Sets the assoc_rssi of this ClientConnectSuccessEvent.


        :param assoc_rssi: The assoc_rssi of this ClientConnectSuccessEvent.  # noqa: E501
        :type: int
        """

        self._assoc_rssi = assoc_rssi

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
        if issubclass(ClientConnectSuccessEvent, dict):
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
        if not isinstance(other, ClientConnectSuccessEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
