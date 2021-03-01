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

class ApElementConfiguration(object):
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
        'element_config_version': 'str',
        'equipment_type': 'EquipmentType',
        'device_mode': 'DeviceMode',
        'getting_ip': 'str',
        'static_ip': 'str',
        'static_ip_mask_cidr': 'int',
        'static_ip_gw': 'str',
        'getting_dns': 'str',
        'static_dns_ip1': 'str',
        'static_dns_ip2': 'str',
        'peer_info_list': 'list[PeerInfo]',
        'device_name': 'str',
        'location_data': 'str',
        'locally_configured_mgmt_vlan': 'int',
        'locally_configured': 'bool',
        'deployment_type': 'DeploymentType',
        'synthetic_client_enabled': 'bool',
        'frame_report_throttle_enabled': 'bool',
        'antenna_type': 'AntennaType',
        'cost_saving_events_enabled': 'bool',
        'forward_mode': 'NetworkForwardMode',
        'radio_map': 'RadioMap',
        'advanced_radio_map': 'AdvancedRadioMap'
    }

    attribute_map = {
        'model_type': 'model_type',
        'element_config_version': 'elementConfigVersion',
        'equipment_type': 'equipmentType',
        'device_mode': 'deviceMode',
        'getting_ip': 'gettingIP',
        'static_ip': 'staticIP',
        'static_ip_mask_cidr': 'staticIpMaskCidr',
        'static_ip_gw': 'staticIpGw',
        'getting_dns': 'gettingDNS',
        'static_dns_ip1': 'staticDnsIp1',
        'static_dns_ip2': 'staticDnsIp2',
        'peer_info_list': 'peerInfoList',
        'device_name': 'deviceName',
        'location_data': 'locationData',
        'locally_configured_mgmt_vlan': 'locallyConfiguredMgmtVlan',
        'locally_configured': 'locallyConfigured',
        'deployment_type': 'deploymentType',
        'synthetic_client_enabled': 'syntheticClientEnabled',
        'frame_report_throttle_enabled': 'frameReportThrottleEnabled',
        'antenna_type': 'antennaType',
        'cost_saving_events_enabled': 'costSavingEventsEnabled',
        'forward_mode': 'forwardMode',
        'radio_map': 'radioMap',
        'advanced_radio_map': 'advancedRadioMap'
    }

    def __init__(self, model_type=None, element_config_version=None, equipment_type=None, device_mode=None, getting_ip=None, static_ip=None, static_ip_mask_cidr=None, static_ip_gw=None, getting_dns=None, static_dns_ip1=None, static_dns_ip2=None, peer_info_list=None, device_name=None, location_data=None, locally_configured_mgmt_vlan=None, locally_configured=None, deployment_type=None, synthetic_client_enabled=None, frame_report_throttle_enabled=None, antenna_type=None, cost_saving_events_enabled=None, forward_mode=None, radio_map=None, advanced_radio_map=None):  # noqa: E501
        """ApElementConfiguration - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._element_config_version = None
        self._equipment_type = None
        self._device_mode = None
        self._getting_ip = None
        self._static_ip = None
        self._static_ip_mask_cidr = None
        self._static_ip_gw = None
        self._getting_dns = None
        self._static_dns_ip1 = None
        self._static_dns_ip2 = None
        self._peer_info_list = None
        self._device_name = None
        self._location_data = None
        self._locally_configured_mgmt_vlan = None
        self._locally_configured = None
        self._deployment_type = None
        self._synthetic_client_enabled = None
        self._frame_report_throttle_enabled = None
        self._antenna_type = None
        self._cost_saving_events_enabled = None
        self._forward_mode = None
        self._radio_map = None
        self._advanced_radio_map = None
        self.discriminator = None
        self.model_type = model_type
        if element_config_version is not None:
            self.element_config_version = element_config_version
        if equipment_type is not None:
            self.equipment_type = equipment_type
        if device_mode is not None:
            self.device_mode = device_mode
        if getting_ip is not None:
            self.getting_ip = getting_ip
        if static_ip is not None:
            self.static_ip = static_ip
        if static_ip_mask_cidr is not None:
            self.static_ip_mask_cidr = static_ip_mask_cidr
        if static_ip_gw is not None:
            self.static_ip_gw = static_ip_gw
        if getting_dns is not None:
            self.getting_dns = getting_dns
        if static_dns_ip1 is not None:
            self.static_dns_ip1 = static_dns_ip1
        if static_dns_ip2 is not None:
            self.static_dns_ip2 = static_dns_ip2
        if peer_info_list is not None:
            self.peer_info_list = peer_info_list
        if device_name is not None:
            self.device_name = device_name
        if location_data is not None:
            self.location_data = location_data
        if locally_configured_mgmt_vlan is not None:
            self.locally_configured_mgmt_vlan = locally_configured_mgmt_vlan
        if locally_configured is not None:
            self.locally_configured = locally_configured
        if deployment_type is not None:
            self.deployment_type = deployment_type
        if synthetic_client_enabled is not None:
            self.synthetic_client_enabled = synthetic_client_enabled
        if frame_report_throttle_enabled is not None:
            self.frame_report_throttle_enabled = frame_report_throttle_enabled
        if antenna_type is not None:
            self.antenna_type = antenna_type
        if cost_saving_events_enabled is not None:
            self.cost_saving_events_enabled = cost_saving_events_enabled
        if forward_mode is not None:
            self.forward_mode = forward_mode
        if radio_map is not None:
            self.radio_map = radio_map
        if advanced_radio_map is not None:
            self.advanced_radio_map = advanced_radio_map

    @property
    def model_type(self):
        """Gets the model_type of this ApElementConfiguration.  # noqa: E501


        :return: The model_type of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this ApElementConfiguration.


        :param model_type: The model_type of this ApElementConfiguration.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def element_config_version(self):
        """Gets the element_config_version of this ApElementConfiguration.  # noqa: E501


        :return: The element_config_version of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._element_config_version

    @element_config_version.setter
    def element_config_version(self, element_config_version):
        """Sets the element_config_version of this ApElementConfiguration.


        :param element_config_version: The element_config_version of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._element_config_version = element_config_version

    @property
    def equipment_type(self):
        """Gets the equipment_type of this ApElementConfiguration.  # noqa: E501


        :return: The equipment_type of this ApElementConfiguration.  # noqa: E501
        :rtype: EquipmentType
        """
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        """Sets the equipment_type of this ApElementConfiguration.


        :param equipment_type: The equipment_type of this ApElementConfiguration.  # noqa: E501
        :type: EquipmentType
        """

        self._equipment_type = equipment_type

    @property
    def device_mode(self):
        """Gets the device_mode of this ApElementConfiguration.  # noqa: E501


        :return: The device_mode of this ApElementConfiguration.  # noqa: E501
        :rtype: DeviceMode
        """
        return self._device_mode

    @device_mode.setter
    def device_mode(self, device_mode):
        """Sets the device_mode of this ApElementConfiguration.


        :param device_mode: The device_mode of this ApElementConfiguration.  # noqa: E501
        :type: DeviceMode
        """

        self._device_mode = device_mode

    @property
    def getting_ip(self):
        """Gets the getting_ip of this ApElementConfiguration.  # noqa: E501


        :return: The getting_ip of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._getting_ip

    @getting_ip.setter
    def getting_ip(self, getting_ip):
        """Sets the getting_ip of this ApElementConfiguration.


        :param getting_ip: The getting_ip of this ApElementConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["dhcp", "manual"]  # noqa: E501
        if getting_ip not in allowed_values:
            raise ValueError(
                "Invalid value for `getting_ip` ({0}), must be one of {1}"  # noqa: E501
                .format(getting_ip, allowed_values)
            )

        self._getting_ip = getting_ip

    @property
    def static_ip(self):
        """Gets the static_ip of this ApElementConfiguration.  # noqa: E501


        :return: The static_ip of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        """Sets the static_ip of this ApElementConfiguration.


        :param static_ip: The static_ip of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._static_ip = static_ip

    @property
    def static_ip_mask_cidr(self):
        """Gets the static_ip_mask_cidr of this ApElementConfiguration.  # noqa: E501


        :return: The static_ip_mask_cidr of this ApElementConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._static_ip_mask_cidr

    @static_ip_mask_cidr.setter
    def static_ip_mask_cidr(self, static_ip_mask_cidr):
        """Sets the static_ip_mask_cidr of this ApElementConfiguration.


        :param static_ip_mask_cidr: The static_ip_mask_cidr of this ApElementConfiguration.  # noqa: E501
        :type: int
        """

        self._static_ip_mask_cidr = static_ip_mask_cidr

    @property
    def static_ip_gw(self):
        """Gets the static_ip_gw of this ApElementConfiguration.  # noqa: E501


        :return: The static_ip_gw of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._static_ip_gw

    @static_ip_gw.setter
    def static_ip_gw(self, static_ip_gw):
        """Sets the static_ip_gw of this ApElementConfiguration.


        :param static_ip_gw: The static_ip_gw of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._static_ip_gw = static_ip_gw

    @property
    def getting_dns(self):
        """Gets the getting_dns of this ApElementConfiguration.  # noqa: E501


        :return: The getting_dns of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._getting_dns

    @getting_dns.setter
    def getting_dns(self, getting_dns):
        """Sets the getting_dns of this ApElementConfiguration.


        :param getting_dns: The getting_dns of this ApElementConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["dhcp", "manual"]  # noqa: E501
        if getting_dns not in allowed_values:
            raise ValueError(
                "Invalid value for `getting_dns` ({0}), must be one of {1}"  # noqa: E501
                .format(getting_dns, allowed_values)
            )

        self._getting_dns = getting_dns

    @property
    def static_dns_ip1(self):
        """Gets the static_dns_ip1 of this ApElementConfiguration.  # noqa: E501


        :return: The static_dns_ip1 of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._static_dns_ip1

    @static_dns_ip1.setter
    def static_dns_ip1(self, static_dns_ip1):
        """Sets the static_dns_ip1 of this ApElementConfiguration.


        :param static_dns_ip1: The static_dns_ip1 of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._static_dns_ip1 = static_dns_ip1

    @property
    def static_dns_ip2(self):
        """Gets the static_dns_ip2 of this ApElementConfiguration.  # noqa: E501


        :return: The static_dns_ip2 of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._static_dns_ip2

    @static_dns_ip2.setter
    def static_dns_ip2(self, static_dns_ip2):
        """Sets the static_dns_ip2 of this ApElementConfiguration.


        :param static_dns_ip2: The static_dns_ip2 of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._static_dns_ip2 = static_dns_ip2

    @property
    def peer_info_list(self):
        """Gets the peer_info_list of this ApElementConfiguration.  # noqa: E501


        :return: The peer_info_list of this ApElementConfiguration.  # noqa: E501
        :rtype: list[PeerInfo]
        """
        return self._peer_info_list

    @peer_info_list.setter
    def peer_info_list(self, peer_info_list):
        """Sets the peer_info_list of this ApElementConfiguration.


        :param peer_info_list: The peer_info_list of this ApElementConfiguration.  # noqa: E501
        :type: list[PeerInfo]
        """

        self._peer_info_list = peer_info_list

    @property
    def device_name(self):
        """Gets the device_name of this ApElementConfiguration.  # noqa: E501


        :return: The device_name of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ApElementConfiguration.


        :param device_name: The device_name of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def location_data(self):
        """Gets the location_data of this ApElementConfiguration.  # noqa: E501


        :return: The location_data of this ApElementConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._location_data

    @location_data.setter
    def location_data(self, location_data):
        """Sets the location_data of this ApElementConfiguration.


        :param location_data: The location_data of this ApElementConfiguration.  # noqa: E501
        :type: str
        """

        self._location_data = location_data

    @property
    def locally_configured_mgmt_vlan(self):
        """Gets the locally_configured_mgmt_vlan of this ApElementConfiguration.  # noqa: E501


        :return: The locally_configured_mgmt_vlan of this ApElementConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._locally_configured_mgmt_vlan

    @locally_configured_mgmt_vlan.setter
    def locally_configured_mgmt_vlan(self, locally_configured_mgmt_vlan):
        """Sets the locally_configured_mgmt_vlan of this ApElementConfiguration.


        :param locally_configured_mgmt_vlan: The locally_configured_mgmt_vlan of this ApElementConfiguration.  # noqa: E501
        :type: int
        """

        self._locally_configured_mgmt_vlan = locally_configured_mgmt_vlan

    @property
    def locally_configured(self):
        """Gets the locally_configured of this ApElementConfiguration.  # noqa: E501


        :return: The locally_configured of this ApElementConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._locally_configured

    @locally_configured.setter
    def locally_configured(self, locally_configured):
        """Sets the locally_configured of this ApElementConfiguration.


        :param locally_configured: The locally_configured of this ApElementConfiguration.  # noqa: E501
        :type: bool
        """

        self._locally_configured = locally_configured

    @property
    def deployment_type(self):
        """Gets the deployment_type of this ApElementConfiguration.  # noqa: E501


        :return: The deployment_type of this ApElementConfiguration.  # noqa: E501
        :rtype: DeploymentType
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this ApElementConfiguration.


        :param deployment_type: The deployment_type of this ApElementConfiguration.  # noqa: E501
        :type: DeploymentType
        """

        self._deployment_type = deployment_type

    @property
    def synthetic_client_enabled(self):
        """Gets the synthetic_client_enabled of this ApElementConfiguration.  # noqa: E501


        :return: The synthetic_client_enabled of this ApElementConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._synthetic_client_enabled

    @synthetic_client_enabled.setter
    def synthetic_client_enabled(self, synthetic_client_enabled):
        """Sets the synthetic_client_enabled of this ApElementConfiguration.


        :param synthetic_client_enabled: The synthetic_client_enabled of this ApElementConfiguration.  # noqa: E501
        :type: bool
        """

        self._synthetic_client_enabled = synthetic_client_enabled

    @property
    def frame_report_throttle_enabled(self):
        """Gets the frame_report_throttle_enabled of this ApElementConfiguration.  # noqa: E501


        :return: The frame_report_throttle_enabled of this ApElementConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._frame_report_throttle_enabled

    @frame_report_throttle_enabled.setter
    def frame_report_throttle_enabled(self, frame_report_throttle_enabled):
        """Sets the frame_report_throttle_enabled of this ApElementConfiguration.


        :param frame_report_throttle_enabled: The frame_report_throttle_enabled of this ApElementConfiguration.  # noqa: E501
        :type: bool
        """

        self._frame_report_throttle_enabled = frame_report_throttle_enabled

    @property
    def antenna_type(self):
        """Gets the antenna_type of this ApElementConfiguration.  # noqa: E501


        :return: The antenna_type of this ApElementConfiguration.  # noqa: E501
        :rtype: AntennaType
        """
        return self._antenna_type

    @antenna_type.setter
    def antenna_type(self, antenna_type):
        """Sets the antenna_type of this ApElementConfiguration.


        :param antenna_type: The antenna_type of this ApElementConfiguration.  # noqa: E501
        :type: AntennaType
        """

        self._antenna_type = antenna_type

    @property
    def cost_saving_events_enabled(self):
        """Gets the cost_saving_events_enabled of this ApElementConfiguration.  # noqa: E501


        :return: The cost_saving_events_enabled of this ApElementConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._cost_saving_events_enabled

    @cost_saving_events_enabled.setter
    def cost_saving_events_enabled(self, cost_saving_events_enabled):
        """Sets the cost_saving_events_enabled of this ApElementConfiguration.


        :param cost_saving_events_enabled: The cost_saving_events_enabled of this ApElementConfiguration.  # noqa: E501
        :type: bool
        """

        self._cost_saving_events_enabled = cost_saving_events_enabled

    @property
    def forward_mode(self):
        """Gets the forward_mode of this ApElementConfiguration.  # noqa: E501


        :return: The forward_mode of this ApElementConfiguration.  # noqa: E501
        :rtype: NetworkForwardMode
        """
        return self._forward_mode

    @forward_mode.setter
    def forward_mode(self, forward_mode):
        """Sets the forward_mode of this ApElementConfiguration.


        :param forward_mode: The forward_mode of this ApElementConfiguration.  # noqa: E501
        :type: NetworkForwardMode
        """

        self._forward_mode = forward_mode

    @property
    def radio_map(self):
        """Gets the radio_map of this ApElementConfiguration.  # noqa: E501


        :return: The radio_map of this ApElementConfiguration.  # noqa: E501
        :rtype: RadioMap
        """
        return self._radio_map

    @radio_map.setter
    def radio_map(self, radio_map):
        """Sets the radio_map of this ApElementConfiguration.


        :param radio_map: The radio_map of this ApElementConfiguration.  # noqa: E501
        :type: RadioMap
        """

        self._radio_map = radio_map

    @property
    def advanced_radio_map(self):
        """Gets the advanced_radio_map of this ApElementConfiguration.  # noqa: E501


        :return: The advanced_radio_map of this ApElementConfiguration.  # noqa: E501
        :rtype: AdvancedRadioMap
        """
        return self._advanced_radio_map

    @advanced_radio_map.setter
    def advanced_radio_map(self, advanced_radio_map):
        """Sets the advanced_radio_map of this ApElementConfiguration.


        :param advanced_radio_map: The advanced_radio_map of this ApElementConfiguration.  # noqa: E501
        :type: AdvancedRadioMap
        """

        self._advanced_radio_map = advanced_radio_map

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
        if issubclass(ApElementConfiguration, dict):
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
        if not isinstance(other, ApElementConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
