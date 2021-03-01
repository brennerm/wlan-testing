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

class SystemEventDataType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    GATEWAYADDEDEVENT = "GatewayAddedEvent"
    GATEWAYCHANGEDEVENT = "GatewayChangedEvent"
    GATEWAYREMOVEDEVENT = "GatewayRemovedEvent"
    CLIENTADDEDEVENT = "ClientAddedEvent"
    CLIENTCHANGEDEVENT = "ClientChangedEvent"
    CLIENTREMOVEDEVENT = "ClientRemovedEvent"
    CUSTOMERADDEDEVENT = "CustomerAddedEvent"
    CUSTOMERCHANGEDEVENT = "CustomerChangedEvent"
    CUSTOMERREMOVEDEVENT = "CustomerRemovedEvent"
    FIRMWAREADDEDEVENT = "FirmwareAddedEvent"
    FIRMWARECHANGEDEVENT = "FirmwareChangedEvent"
    FIRMWAREREMOVEDEVENT = "FirmwareRemovedEvent"
    LOCATIONADDEDEVENT = "LocationAddedEvent"
    LOCATIONCHANGEDEVENT = "LocationChangedEvent"
    LOCATIONREMOVEDEVENT = "LocationRemovedEvent"
    PORTALUSERADDEDEVENT = "PortalUserAddedEvent"
    PORTALUSERCHANGEDEVENT = "PortalUserChangedEvent"
    PORTALUSERREMOVEDEVENT = "PortalUserRemovedEvent"
    PROFILEADDEDEVENT = "ProfileAddedEvent"
    PROFILECHANGEDEVENT = "ProfileChangedEvent"
    PROFILEREMOVEDEVENT = "ProfileRemovedEvent"
    ROUTINGADDEDEVENT = "RoutingAddedEvent"
    ROUTINGCHANGEDEVENT = "RoutingChangedEvent"
    ROUTINGREMOVEDEVENT = "RoutingRemovedEvent"
    ALARMADDEDEVENT = "AlarmAddedEvent"
    ALARMCHANGEDEVENT = "AlarmChangedEvent"
    ALARMREMOVEDEVENT = "AlarmRemovedEvent"
    CLIENTSESSIONADDEDEVENT = "ClientSessionAddedEvent"
    CLIENTSESSIONCHANGEDEVENT = "ClientSessionChangedEvent"
    CLIENTSESSIONREMOVEDEVENT = "ClientSessionRemovedEvent"
    EQUIPMENTADDEDEVENT = "EquipmentAddedEvent"
    EQUIPMENTCHANGEDEVENT = "EquipmentChangedEvent"
    EQUIPMENTREMOVEDEVENT = "EquipmentRemovedEvent"
    STATUSCHANGEDEVENT = "StatusChangedEvent"
    STATUSREMOVEDEVENT = "StatusRemovedEvent"
    DHCPACKEVENT = "DhcpAckEvent"
    DHCPNAKEVENT = "DhcpNakEvent"
    DHCPDECLINEEVENT = "DhcpDeclineEvent"
    DHCPDISCOVEREVENT = "DhcpDiscoverEvent"
    DHCPINFORMEVENT = "DhcpInformEvent"
    DHCPOFFEREVENT = "DhcpOfferEvent"
    DHCPREQUESTEVENT = "DhcpRequestEvent"
    CLIENTASSOCEVENT = "ClientAssocEvent"
    CLIENTCONNECTSUCCESSEVENT = "ClientConnectSuccessEvent"
    CLIENTFAILUREEVENT = "ClientFailureEvent"
    CLIENTIDEVENT = "ClientIdEvent"
    CLIENTTIMEOUTEVENT = "ClientTimeoutEvent"
    CLIENTAUTHEVENT = "ClientAuthEvent"
    CLIENTDISCONNECTEVENT = "ClientDisconnectEvent"
    CLIENTFIRSTDATAEVENT = "ClientFirstDataEvent"
    CLIENTIPADDRESSEVENT = "ClientIpAddressEvent"
    REALTIMECHANNELHOPEVENT = "RealTimeChannelHopEvent"
    REALTIMESIPCALLEVENTWITHSTATS = "RealTimeSipCallEventWithStats"
    REALTIMESIPCALLREPORTEVENT = "RealTimeSipCallReportEvent"
    REALTIMESIPCALLSTARTEVENT = "RealTimeSipCallStartEvent"
    REALTIMESIPCALLSTOPEVENT = "RealTimeSipCallStopEvent"
    REALTIMESTREAMINGSTARTEVENT = "RealTimeStreamingStartEvent"
    REALTIMESTREAMINGSTARTSESSIONEVENT = "RealTimeStreamingStartSessionEvent"
    REALTIMESTREAMINGSTOPEVENT = "RealTimeStreamingStopEvent"
    UNSERIALIZABLESYSTEMEVENT = "UnserializableSystemEvent"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """SystemEventDataType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(SystemEventDataType, dict):
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
        if not isinstance(other, SystemEventDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
