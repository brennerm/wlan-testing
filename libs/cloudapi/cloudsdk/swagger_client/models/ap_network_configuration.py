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
from swagger_client.models.profile_details import ProfileDetails  # noqa: F401,E501

class ApNetworkConfiguration(ProfileDetails):
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
        'network_config_version': 'str',
        'equipment_type': 'str',
        'vlan_native': 'bool',
        'vlan': 'int',
        'ntp_server': 'ApNetworkConfigurationNtpServer',
        'syslog_relay': 'SyslogRelay',
        'rtls_settings': 'RtlsSettings',
        'synthetic_client_enabled': 'bool',
        'led_control_enabled': 'bool',
        'equipment_discovery': 'bool',
        'gre_tunnel_configurations': 'list[GreTunnelConfiguration]',
        'radio_map': 'RadioProfileConfigurationMap'
    }
    if hasattr(ProfileDetails, "swagger_types"):
        swagger_types.update(ProfileDetails.swagger_types)

    attribute_map = {
        'model_type': 'model_type',
        'network_config_version': 'networkConfigVersion',
        'equipment_type': 'equipmentType',
        'vlan_native': 'vlanNative',
        'vlan': 'vlan',
        'ntp_server': 'ntpServer',
        'syslog_relay': 'syslogRelay',
        'rtls_settings': 'rtlsSettings',
        'synthetic_client_enabled': 'syntheticClientEnabled',
        'led_control_enabled': 'ledControlEnabled',
        'equipment_discovery': 'equipmentDiscovery',
        'gre_tunnel_configurations': 'greTunnelConfigurations',
        'radio_map': 'radioMap'
    }
    if hasattr(ProfileDetails, "attribute_map"):
        attribute_map.update(ProfileDetails.attribute_map)

    def __init__(self, model_type=None, network_config_version=None, equipment_type=None, vlan_native=None, vlan=None, ntp_server=None, syslog_relay=None, rtls_settings=None, synthetic_client_enabled=None, led_control_enabled=None, equipment_discovery=None, gre_tunnel_configurations=None, radio_map=None, *args, **kwargs):  # noqa: E501
        """ApNetworkConfiguration - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._network_config_version = None
        self._equipment_type = None
        self._vlan_native = None
        self._vlan = None
        self._ntp_server = None
        self._syslog_relay = None
        self._rtls_settings = None
        self._synthetic_client_enabled = None
        self._led_control_enabled = None
        self._equipment_discovery = None
        self._gre_tunnel_configurations = None
        self._radio_map = None
        self.discriminator = None
        if model_type is not None:
            self.model_type = model_type
        if network_config_version is not None:
            self.network_config_version = network_config_version
        if equipment_type is not None:
            self.equipment_type = equipment_type
        if vlan_native is not None:
            self.vlan_native = vlan_native
        if vlan is not None:
            self.vlan = vlan
        if ntp_server is not None:
            self.ntp_server = ntp_server
        if syslog_relay is not None:
            self.syslog_relay = syslog_relay
        if rtls_settings is not None:
            self.rtls_settings = rtls_settings
        if synthetic_client_enabled is not None:
            self.synthetic_client_enabled = synthetic_client_enabled
        if led_control_enabled is not None:
            self.led_control_enabled = led_control_enabled
        if equipment_discovery is not None:
            self.equipment_discovery = equipment_discovery
        if gre_tunnel_configurations is not None:
            self.gre_tunnel_configurations = gre_tunnel_configurations
        if radio_map is not None:
            self.radio_map = radio_map
        ProfileDetails.__init__(self, *args, **kwargs)

    @property
    def model_type(self):
        """Gets the model_type of this ApNetworkConfiguration.  # noqa: E501


        :return: The model_type of this ApNetworkConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ApNetworkConfiguration.


        :param model_type: The model_type of this ApNetworkConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["ApNetworkConfiguration"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def network_config_version(self):
        """Gets the network_config_version of this ApNetworkConfiguration.  # noqa: E501


        :return: The network_config_version of this ApNetworkConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._network_config_version

    @network_config_version.setter
    def network_config_version(self, network_config_version):
        """Sets the network_config_version of this ApNetworkConfiguration.


        :param network_config_version: The network_config_version of this ApNetworkConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["AP-1"]  # noqa: E501
        if network_config_version not in allowed_values:
            raise ValueError(
                "Invalid value for `network_config_version` ({0}), must be one of {1}"  # noqa: E501
                .format(network_config_version, allowed_values)
            )

        self._network_config_version = network_config_version

    @property
    def equipment_type(self):
        """Gets the equipment_type of this ApNetworkConfiguration.  # noqa: E501


        :return: The equipment_type of this ApNetworkConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        """Sets the equipment_type of this ApNetworkConfiguration.


        :param equipment_type: The equipment_type of this ApNetworkConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["AP"]  # noqa: E501
        if equipment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `equipment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(equipment_type, allowed_values)
            )

        self._equipment_type = equipment_type

    @property
    def vlan_native(self):
        """Gets the vlan_native of this ApNetworkConfiguration.  # noqa: E501


        :return: The vlan_native of this ApNetworkConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._vlan_native

    @vlan_native.setter
    def vlan_native(self, vlan_native):
        """Sets the vlan_native of this ApNetworkConfiguration.


        :param vlan_native: The vlan_native of this ApNetworkConfiguration.  # noqa: E501
        :type: bool
        """

        self._vlan_native = vlan_native

    @property
    def vlan(self):
        """Gets the vlan of this ApNetworkConfiguration.  # noqa: E501


        :return: The vlan of this ApNetworkConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this ApNetworkConfiguration.


        :param vlan: The vlan of this ApNetworkConfiguration.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def ntp_server(self):
        """Gets the ntp_server of this ApNetworkConfiguration.  # noqa: E501


        :return: The ntp_server of this ApNetworkConfiguration.  # noqa: E501
        :rtype: ApNetworkConfigurationNtpServer
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """Sets the ntp_server of this ApNetworkConfiguration.


        :param ntp_server: The ntp_server of this ApNetworkConfiguration.  # noqa: E501
        :type: ApNetworkConfigurationNtpServer
        """

        self._ntp_server = ntp_server

    @property
    def syslog_relay(self):
        """Gets the syslog_relay of this ApNetworkConfiguration.  # noqa: E501


        :return: The syslog_relay of this ApNetworkConfiguration.  # noqa: E501
        :rtype: SyslogRelay
        """
        return self._syslog_relay

    @syslog_relay.setter
    def syslog_relay(self, syslog_relay):
        """Sets the syslog_relay of this ApNetworkConfiguration.


        :param syslog_relay: The syslog_relay of this ApNetworkConfiguration.  # noqa: E501
        :type: SyslogRelay
        """

        self._syslog_relay = syslog_relay

    @property
    def rtls_settings(self):
        """Gets the rtls_settings of this ApNetworkConfiguration.  # noqa: E501


        :return: The rtls_settings of this ApNetworkConfiguration.  # noqa: E501
        :rtype: RtlsSettings
        """
        return self._rtls_settings

    @rtls_settings.setter
    def rtls_settings(self, rtls_settings):
        """Sets the rtls_settings of this ApNetworkConfiguration.


        :param rtls_settings: The rtls_settings of this ApNetworkConfiguration.  # noqa: E501
        :type: RtlsSettings
        """

        self._rtls_settings = rtls_settings

    @property
    def synthetic_client_enabled(self):
        """Gets the synthetic_client_enabled of this ApNetworkConfiguration.  # noqa: E501


        :return: The synthetic_client_enabled of this ApNetworkConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._synthetic_client_enabled

    @synthetic_client_enabled.setter
    def synthetic_client_enabled(self, synthetic_client_enabled):
        """Sets the synthetic_client_enabled of this ApNetworkConfiguration.


        :param synthetic_client_enabled: The synthetic_client_enabled of this ApNetworkConfiguration.  # noqa: E501
        :type: bool
        """

        self._synthetic_client_enabled = synthetic_client_enabled

    @property
    def led_control_enabled(self):
        """Gets the led_control_enabled of this ApNetworkConfiguration.  # noqa: E501


        :return: The led_control_enabled of this ApNetworkConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._led_control_enabled

    @led_control_enabled.setter
    def led_control_enabled(self, led_control_enabled):
        """Sets the led_control_enabled of this ApNetworkConfiguration.


        :param led_control_enabled: The led_control_enabled of this ApNetworkConfiguration.  # noqa: E501
        :type: bool
        """

        self._led_control_enabled = led_control_enabled

    @property
    def equipment_discovery(self):
        """Gets the equipment_discovery of this ApNetworkConfiguration.  # noqa: E501


        :return: The equipment_discovery of this ApNetworkConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._equipment_discovery

    @equipment_discovery.setter
    def equipment_discovery(self, equipment_discovery):
        """Sets the equipment_discovery of this ApNetworkConfiguration.


        :param equipment_discovery: The equipment_discovery of this ApNetworkConfiguration.  # noqa: E501
        :type: bool
        """

        self._equipment_discovery = equipment_discovery

    @property
    def gre_tunnel_configurations(self):
        """Gets the gre_tunnel_configurations of this ApNetworkConfiguration.  # noqa: E501


        :return: The gre_tunnel_configurations of this ApNetworkConfiguration.  # noqa: E501
        :rtype: list[GreTunnelConfiguration]
        """
        return self._gre_tunnel_configurations

    @gre_tunnel_configurations.setter
    def gre_tunnel_configurations(self, gre_tunnel_configurations):
        """Sets the gre_tunnel_configurations of this ApNetworkConfiguration.


        :param gre_tunnel_configurations: The gre_tunnel_configurations of this ApNetworkConfiguration.  # noqa: E501
        :type: list[GreTunnelConfiguration]
        """

        self._gre_tunnel_configurations = gre_tunnel_configurations

    @property
    def radio_map(self):
        """Gets the radio_map of this ApNetworkConfiguration.  # noqa: E501


        :return: The radio_map of this ApNetworkConfiguration.  # noqa: E501
        :rtype: RadioProfileConfigurationMap
        """
        return self._radio_map

    @radio_map.setter
    def radio_map(self, radio_map):
        """Sets the radio_map of this ApNetworkConfiguration.


        :param radio_map: The radio_map of this ApNetworkConfiguration.  # noqa: E501
        :type: RadioProfileConfigurationMap
        """

        self._radio_map = radio_map

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
        if issubclass(ApNetworkConfiguration, dict):
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
        if not isinstance(other, ApNetworkConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
