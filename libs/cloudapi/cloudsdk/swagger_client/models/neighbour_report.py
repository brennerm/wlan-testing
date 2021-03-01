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

class NeighbourReport(object):
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
        'mac_address': 'MacAddress',
        'ssid': 'str',
        'beacon_interval': 'int',
        'network_type': 'NetworkType',
        'privacy': 'bool',
        'radio_type_radio_type': 'RadioType',
        'channel': 'int',
        'rate': 'int',
        'rssi': 'int',
        'signal': 'int',
        'scan_time_in_seconds': 'int',
        'n_mode': 'bool',
        'ac_mode': 'bool',
        'b_mode': 'bool',
        'packet_type': 'NeighborScanPacketType',
        'secure_mode': 'DetectedAuthMode'
    }

    attribute_map = {
        'mac_address': 'macAddress',
        'ssid': 'ssid',
        'beacon_interval': 'beaconInterval',
        'network_type': 'networkType',
        'privacy': 'privacy',
        'radio_type_radio_type': 'RadioType radioType',
        'channel': 'channel',
        'rate': 'rate',
        'rssi': 'rssi',
        'signal': 'signal',
        'scan_time_in_seconds': 'scanTimeInSeconds',
        'n_mode': 'nMode',
        'ac_mode': 'acMode',
        'b_mode': 'bMode',
        'packet_type': 'packetType',
        'secure_mode': 'secureMode'
    }

    def __init__(self, mac_address=None, ssid=None, beacon_interval=None, network_type=None, privacy=None, radio_type_radio_type=None, channel=None, rate=None, rssi=None, signal=None, scan_time_in_seconds=None, n_mode=None, ac_mode=None, b_mode=None, packet_type=None, secure_mode=None):  # noqa: E501
        """NeighbourReport - a model defined in Swagger"""  # noqa: E501
        self._mac_address = None
        self._ssid = None
        self._beacon_interval = None
        self._network_type = None
        self._privacy = None
        self._radio_type_radio_type = None
        self._channel = None
        self._rate = None
        self._rssi = None
        self._signal = None
        self._scan_time_in_seconds = None
        self._n_mode = None
        self._ac_mode = None
        self._b_mode = None
        self._packet_type = None
        self._secure_mode = None
        self.discriminator = None
        if mac_address is not None:
            self.mac_address = mac_address
        if ssid is not None:
            self.ssid = ssid
        if beacon_interval is not None:
            self.beacon_interval = beacon_interval
        if network_type is not None:
            self.network_type = network_type
        if privacy is not None:
            self.privacy = privacy
        if radio_type_radio_type is not None:
            self.radio_type_radio_type = radio_type_radio_type
        if channel is not None:
            self.channel = channel
        if rate is not None:
            self.rate = rate
        if rssi is not None:
            self.rssi = rssi
        if signal is not None:
            self.signal = signal
        if scan_time_in_seconds is not None:
            self.scan_time_in_seconds = scan_time_in_seconds
        if n_mode is not None:
            self.n_mode = n_mode
        if ac_mode is not None:
            self.ac_mode = ac_mode
        if b_mode is not None:
            self.b_mode = b_mode
        if packet_type is not None:
            self.packet_type = packet_type
        if secure_mode is not None:
            self.secure_mode = secure_mode

    @property
    def mac_address(self):
        """Gets the mac_address of this NeighbourReport.  # noqa: E501


        :return: The mac_address of this NeighbourReport.  # noqa: E501
        :rtype: MacAddress
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NeighbourReport.


        :param mac_address: The mac_address of this NeighbourReport.  # noqa: E501
        :type: MacAddress
        """

        self._mac_address = mac_address

    @property
    def ssid(self):
        """Gets the ssid of this NeighbourReport.  # noqa: E501


        :return: The ssid of this NeighbourReport.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this NeighbourReport.


        :param ssid: The ssid of this NeighbourReport.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def beacon_interval(self):
        """Gets the beacon_interval of this NeighbourReport.  # noqa: E501


        :return: The beacon_interval of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._beacon_interval

    @beacon_interval.setter
    def beacon_interval(self, beacon_interval):
        """Sets the beacon_interval of this NeighbourReport.


        :param beacon_interval: The beacon_interval of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._beacon_interval = beacon_interval

    @property
    def network_type(self):
        """Gets the network_type of this NeighbourReport.  # noqa: E501


        :return: The network_type of this NeighbourReport.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this NeighbourReport.


        :param network_type: The network_type of this NeighbourReport.  # noqa: E501
        :type: NetworkType
        """

        self._network_type = network_type

    @property
    def privacy(self):
        """Gets the privacy of this NeighbourReport.  # noqa: E501


        :return: The privacy of this NeighbourReport.  # noqa: E501
        :rtype: bool
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this NeighbourReport.


        :param privacy: The privacy of this NeighbourReport.  # noqa: E501
        :type: bool
        """

        self._privacy = privacy

    @property
    def radio_type_radio_type(self):
        """Gets the radio_type_radio_type of this NeighbourReport.  # noqa: E501


        :return: The radio_type_radio_type of this NeighbourReport.  # noqa: E501
        :rtype: RadioType
        """
        return self._radio_type_radio_type

    @radio_type_radio_type.setter
    def radio_type_radio_type(self, radio_type_radio_type):
        """Sets the radio_type_radio_type of this NeighbourReport.


        :param radio_type_radio_type: The radio_type_radio_type of this NeighbourReport.  # noqa: E501
        :type: RadioType
        """

        self._radio_type_radio_type = radio_type_radio_type

    @property
    def channel(self):
        """Gets the channel of this NeighbourReport.  # noqa: E501


        :return: The channel of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this NeighbourReport.


        :param channel: The channel of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def rate(self):
        """Gets the rate of this NeighbourReport.  # noqa: E501


        :return: The rate of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this NeighbourReport.


        :param rate: The rate of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._rate = rate

    @property
    def rssi(self):
        """Gets the rssi of this NeighbourReport.  # noqa: E501


        :return: The rssi of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """Sets the rssi of this NeighbourReport.


        :param rssi: The rssi of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._rssi = rssi

    @property
    def signal(self):
        """Gets the signal of this NeighbourReport.  # noqa: E501


        :return: The signal of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """Sets the signal of this NeighbourReport.


        :param signal: The signal of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._signal = signal

    @property
    def scan_time_in_seconds(self):
        """Gets the scan_time_in_seconds of this NeighbourReport.  # noqa: E501


        :return: The scan_time_in_seconds of this NeighbourReport.  # noqa: E501
        :rtype: int
        """
        return self._scan_time_in_seconds

    @scan_time_in_seconds.setter
    def scan_time_in_seconds(self, scan_time_in_seconds):
        """Sets the scan_time_in_seconds of this NeighbourReport.


        :param scan_time_in_seconds: The scan_time_in_seconds of this NeighbourReport.  # noqa: E501
        :type: int
        """

        self._scan_time_in_seconds = scan_time_in_seconds

    @property
    def n_mode(self):
        """Gets the n_mode of this NeighbourReport.  # noqa: E501


        :return: The n_mode of this NeighbourReport.  # noqa: E501
        :rtype: bool
        """
        return self._n_mode

    @n_mode.setter
    def n_mode(self, n_mode):
        """Sets the n_mode of this NeighbourReport.


        :param n_mode: The n_mode of this NeighbourReport.  # noqa: E501
        :type: bool
        """

        self._n_mode = n_mode

    @property
    def ac_mode(self):
        """Gets the ac_mode of this NeighbourReport.  # noqa: E501


        :return: The ac_mode of this NeighbourReport.  # noqa: E501
        :rtype: bool
        """
        return self._ac_mode

    @ac_mode.setter
    def ac_mode(self, ac_mode):
        """Sets the ac_mode of this NeighbourReport.


        :param ac_mode: The ac_mode of this NeighbourReport.  # noqa: E501
        :type: bool
        """

        self._ac_mode = ac_mode

    @property
    def b_mode(self):
        """Gets the b_mode of this NeighbourReport.  # noqa: E501


        :return: The b_mode of this NeighbourReport.  # noqa: E501
        :rtype: bool
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        """Sets the b_mode of this NeighbourReport.


        :param b_mode: The b_mode of this NeighbourReport.  # noqa: E501
        :type: bool
        """

        self._b_mode = b_mode

    @property
    def packet_type(self):
        """Gets the packet_type of this NeighbourReport.  # noqa: E501


        :return: The packet_type of this NeighbourReport.  # noqa: E501
        :rtype: NeighborScanPacketType
        """
        return self._packet_type

    @packet_type.setter
    def packet_type(self, packet_type):
        """Sets the packet_type of this NeighbourReport.


        :param packet_type: The packet_type of this NeighbourReport.  # noqa: E501
        :type: NeighborScanPacketType
        """

        self._packet_type = packet_type

    @property
    def secure_mode(self):
        """Gets the secure_mode of this NeighbourReport.  # noqa: E501


        :return: The secure_mode of this NeighbourReport.  # noqa: E501
        :rtype: DetectedAuthMode
        """
        return self._secure_mode

    @secure_mode.setter
    def secure_mode(self, secure_mode):
        """Sets the secure_mode of this NeighbourReport.


        :param secure_mode: The secure_mode of this NeighbourReport.  # noqa: E501
        :type: DetectedAuthMode
        """

        self._secure_mode = secure_mode

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
        if issubclass(NeighbourReport, dict):
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
        if not isinstance(other, NeighbourReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
