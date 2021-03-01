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

class CaptivePortalConfiguration(ProfileDetails):
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
        'browser_title': 'str',
        'header_content': 'str',
        'user_acceptance_policy': 'str',
        'success_page_markdown_text': 'str',
        'redirect_url': 'str',
        'external_captive_portal_url': 'str',
        'session_timeout_in_minutes': 'int',
        'logo_file': 'ManagedFileInfo',
        'background_file': 'ManagedFileInfo',
        'walled_garden_allowlist': 'list[str]',
        'username_password_file': 'ManagedFileInfo',
        'authentication_type': 'CaptivePortalAuthenticationType',
        'radius_auth_method': 'RadiusAuthenticationMethod',
        'max_users_with_same_credentials': 'int',
        'external_policy_file': 'ManagedFileInfo',
        'background_position': 'BackgroundPosition',
        'background_repeat': 'BackgroundRepeat',
        'radius_service_id': 'int',
        'expiry_type': 'SessionExpiryType',
        'user_list': 'list[TimedAccessUserRecord]',
        'mac_allow_list': 'list[MacAllowlistRecord]'
    }
    if hasattr(ProfileDetails, "swagger_types"):
        swagger_types.update(ProfileDetails.swagger_types)

    attribute_map = {
        'model_type': 'model_type',
        'browser_title': 'browserTitle',
        'header_content': 'headerContent',
        'user_acceptance_policy': 'userAcceptancePolicy',
        'success_page_markdown_text': 'successPageMarkdownText',
        'redirect_url': 'redirectURL',
        'external_captive_portal_url': 'externalCaptivePortalURL',
        'session_timeout_in_minutes': 'sessionTimeoutInMinutes',
        'logo_file': 'logoFile',
        'background_file': 'backgroundFile',
        'walled_garden_allowlist': 'walledGardenAllowlist',
        'username_password_file': 'usernamePasswordFile',
        'authentication_type': 'authenticationType',
        'radius_auth_method': 'radiusAuthMethod',
        'max_users_with_same_credentials': 'maxUsersWithSameCredentials',
        'external_policy_file': 'externalPolicyFile',
        'background_position': 'backgroundPosition',
        'background_repeat': 'backgroundRepeat',
        'radius_service_id': 'radiusServiceId',
        'expiry_type': 'expiryType',
        'user_list': 'userList',
        'mac_allow_list': 'macAllowList'
    }
    if hasattr(ProfileDetails, "attribute_map"):
        attribute_map.update(ProfileDetails.attribute_map)

    def __init__(self, model_type=None, browser_title=None, header_content=None, user_acceptance_policy=None, success_page_markdown_text=None, redirect_url=None, external_captive_portal_url=None, session_timeout_in_minutes=None, logo_file=None, background_file=None, walled_garden_allowlist=None, username_password_file=None, authentication_type=None, radius_auth_method=None, max_users_with_same_credentials=None, external_policy_file=None, background_position=None, background_repeat=None, radius_service_id=None, expiry_type=None, user_list=None, mac_allow_list=None, *args, **kwargs):  # noqa: E501
        """CaptivePortalConfiguration - a model defined in Swagger"""  # noqa: E501
        self._model_type = None
        self._browser_title = None
        self._header_content = None
        self._user_acceptance_policy = None
        self._success_page_markdown_text = None
        self._redirect_url = None
        self._external_captive_portal_url = None
        self._session_timeout_in_minutes = None
        self._logo_file = None
        self._background_file = None
        self._walled_garden_allowlist = None
        self._username_password_file = None
        self._authentication_type = None
        self._radius_auth_method = None
        self._max_users_with_same_credentials = None
        self._external_policy_file = None
        self._background_position = None
        self._background_repeat = None
        self._radius_service_id = None
        self._expiry_type = None
        self._user_list = None
        self._mac_allow_list = None
        self.discriminator = None
        if model_type is not None:
            self.model_type = model_type
        if browser_title is not None:
            self.browser_title = browser_title
        if header_content is not None:
            self.header_content = header_content
        if user_acceptance_policy is not None:
            self.user_acceptance_policy = user_acceptance_policy
        if success_page_markdown_text is not None:
            self.success_page_markdown_text = success_page_markdown_text
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if external_captive_portal_url is not None:
            self.external_captive_portal_url = external_captive_portal_url
        if session_timeout_in_minutes is not None:
            self.session_timeout_in_minutes = session_timeout_in_minutes
        if logo_file is not None:
            self.logo_file = logo_file
        if background_file is not None:
            self.background_file = background_file
        if walled_garden_allowlist is not None:
            self.walled_garden_allowlist = walled_garden_allowlist
        if username_password_file is not None:
            self.username_password_file = username_password_file
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if radius_auth_method is not None:
            self.radius_auth_method = radius_auth_method
        if max_users_with_same_credentials is not None:
            self.max_users_with_same_credentials = max_users_with_same_credentials
        if external_policy_file is not None:
            self.external_policy_file = external_policy_file
        if background_position is not None:
            self.background_position = background_position
        if background_repeat is not None:
            self.background_repeat = background_repeat
        if radius_service_id is not None:
            self.radius_service_id = radius_service_id
        if expiry_type is not None:
            self.expiry_type = expiry_type
        if user_list is not None:
            self.user_list = user_list
        if mac_allow_list is not None:
            self.mac_allow_list = mac_allow_list
        ProfileDetails.__init__(self, *args, **kwargs)

    @property
    def model_type(self):
        """Gets the model_type of this CaptivePortalConfiguration.  # noqa: E501


        :return: The model_type of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this CaptivePortalConfiguration.


        :param model_type: The model_type of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["CaptivePortalConfiguration"]  # noqa: E501
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"  # noqa: E501
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

    @property
    def browser_title(self):
        """Gets the browser_title of this CaptivePortalConfiguration.  # noqa: E501


        :return: The browser_title of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._browser_title

    @browser_title.setter
    def browser_title(self, browser_title):
        """Sets the browser_title of this CaptivePortalConfiguration.


        :param browser_title: The browser_title of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._browser_title = browser_title

    @property
    def header_content(self):
        """Gets the header_content of this CaptivePortalConfiguration.  # noqa: E501


        :return: The header_content of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._header_content

    @header_content.setter
    def header_content(self, header_content):
        """Sets the header_content of this CaptivePortalConfiguration.


        :param header_content: The header_content of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._header_content = header_content

    @property
    def user_acceptance_policy(self):
        """Gets the user_acceptance_policy of this CaptivePortalConfiguration.  # noqa: E501


        :return: The user_acceptance_policy of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._user_acceptance_policy

    @user_acceptance_policy.setter
    def user_acceptance_policy(self, user_acceptance_policy):
        """Sets the user_acceptance_policy of this CaptivePortalConfiguration.


        :param user_acceptance_policy: The user_acceptance_policy of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._user_acceptance_policy = user_acceptance_policy

    @property
    def success_page_markdown_text(self):
        """Gets the success_page_markdown_text of this CaptivePortalConfiguration.  # noqa: E501


        :return: The success_page_markdown_text of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._success_page_markdown_text

    @success_page_markdown_text.setter
    def success_page_markdown_text(self, success_page_markdown_text):
        """Sets the success_page_markdown_text of this CaptivePortalConfiguration.


        :param success_page_markdown_text: The success_page_markdown_text of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._success_page_markdown_text = success_page_markdown_text

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CaptivePortalConfiguration.  # noqa: E501


        :return: The redirect_url of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CaptivePortalConfiguration.


        :param redirect_url: The redirect_url of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def external_captive_portal_url(self):
        """Gets the external_captive_portal_url of this CaptivePortalConfiguration.  # noqa: E501


        :return: The external_captive_portal_url of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._external_captive_portal_url

    @external_captive_portal_url.setter
    def external_captive_portal_url(self, external_captive_portal_url):
        """Sets the external_captive_portal_url of this CaptivePortalConfiguration.


        :param external_captive_portal_url: The external_captive_portal_url of this CaptivePortalConfiguration.  # noqa: E501
        :type: str
        """

        self._external_captive_portal_url = external_captive_portal_url

    @property
    def session_timeout_in_minutes(self):
        """Gets the session_timeout_in_minutes of this CaptivePortalConfiguration.  # noqa: E501


        :return: The session_timeout_in_minutes of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._session_timeout_in_minutes

    @session_timeout_in_minutes.setter
    def session_timeout_in_minutes(self, session_timeout_in_minutes):
        """Sets the session_timeout_in_minutes of this CaptivePortalConfiguration.


        :param session_timeout_in_minutes: The session_timeout_in_minutes of this CaptivePortalConfiguration.  # noqa: E501
        :type: int
        """

        self._session_timeout_in_minutes = session_timeout_in_minutes

    @property
    def logo_file(self):
        """Gets the logo_file of this CaptivePortalConfiguration.  # noqa: E501


        :return: The logo_file of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: ManagedFileInfo
        """
        return self._logo_file

    @logo_file.setter
    def logo_file(self, logo_file):
        """Sets the logo_file of this CaptivePortalConfiguration.


        :param logo_file: The logo_file of this CaptivePortalConfiguration.  # noqa: E501
        :type: ManagedFileInfo
        """

        self._logo_file = logo_file

    @property
    def background_file(self):
        """Gets the background_file of this CaptivePortalConfiguration.  # noqa: E501


        :return: The background_file of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: ManagedFileInfo
        """
        return self._background_file

    @background_file.setter
    def background_file(self, background_file):
        """Sets the background_file of this CaptivePortalConfiguration.


        :param background_file: The background_file of this CaptivePortalConfiguration.  # noqa: E501
        :type: ManagedFileInfo
        """

        self._background_file = background_file

    @property
    def walled_garden_allowlist(self):
        """Gets the walled_garden_allowlist of this CaptivePortalConfiguration.  # noqa: E501


        :return: The walled_garden_allowlist of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._walled_garden_allowlist

    @walled_garden_allowlist.setter
    def walled_garden_allowlist(self, walled_garden_allowlist):
        """Sets the walled_garden_allowlist of this CaptivePortalConfiguration.


        :param walled_garden_allowlist: The walled_garden_allowlist of this CaptivePortalConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._walled_garden_allowlist = walled_garden_allowlist

    @property
    def username_password_file(self):
        """Gets the username_password_file of this CaptivePortalConfiguration.  # noqa: E501


        :return: The username_password_file of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: ManagedFileInfo
        """
        return self._username_password_file

    @username_password_file.setter
    def username_password_file(self, username_password_file):
        """Sets the username_password_file of this CaptivePortalConfiguration.


        :param username_password_file: The username_password_file of this CaptivePortalConfiguration.  # noqa: E501
        :type: ManagedFileInfo
        """

        self._username_password_file = username_password_file

    @property
    def authentication_type(self):
        """Gets the authentication_type of this CaptivePortalConfiguration.  # noqa: E501


        :return: The authentication_type of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: CaptivePortalAuthenticationType
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this CaptivePortalConfiguration.


        :param authentication_type: The authentication_type of this CaptivePortalConfiguration.  # noqa: E501
        :type: CaptivePortalAuthenticationType
        """

        self._authentication_type = authentication_type

    @property
    def radius_auth_method(self):
        """Gets the radius_auth_method of this CaptivePortalConfiguration.  # noqa: E501


        :return: The radius_auth_method of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: RadiusAuthenticationMethod
        """
        return self._radius_auth_method

    @radius_auth_method.setter
    def radius_auth_method(self, radius_auth_method):
        """Sets the radius_auth_method of this CaptivePortalConfiguration.


        :param radius_auth_method: The radius_auth_method of this CaptivePortalConfiguration.  # noqa: E501
        :type: RadiusAuthenticationMethod
        """

        self._radius_auth_method = radius_auth_method

    @property
    def max_users_with_same_credentials(self):
        """Gets the max_users_with_same_credentials of this CaptivePortalConfiguration.  # noqa: E501


        :return: The max_users_with_same_credentials of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_users_with_same_credentials

    @max_users_with_same_credentials.setter
    def max_users_with_same_credentials(self, max_users_with_same_credentials):
        """Sets the max_users_with_same_credentials of this CaptivePortalConfiguration.


        :param max_users_with_same_credentials: The max_users_with_same_credentials of this CaptivePortalConfiguration.  # noqa: E501
        :type: int
        """

        self._max_users_with_same_credentials = max_users_with_same_credentials

    @property
    def external_policy_file(self):
        """Gets the external_policy_file of this CaptivePortalConfiguration.  # noqa: E501


        :return: The external_policy_file of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: ManagedFileInfo
        """
        return self._external_policy_file

    @external_policy_file.setter
    def external_policy_file(self, external_policy_file):
        """Sets the external_policy_file of this CaptivePortalConfiguration.


        :param external_policy_file: The external_policy_file of this CaptivePortalConfiguration.  # noqa: E501
        :type: ManagedFileInfo
        """

        self._external_policy_file = external_policy_file

    @property
    def background_position(self):
        """Gets the background_position of this CaptivePortalConfiguration.  # noqa: E501


        :return: The background_position of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: BackgroundPosition
        """
        return self._background_position

    @background_position.setter
    def background_position(self, background_position):
        """Sets the background_position of this CaptivePortalConfiguration.


        :param background_position: The background_position of this CaptivePortalConfiguration.  # noqa: E501
        :type: BackgroundPosition
        """

        self._background_position = background_position

    @property
    def background_repeat(self):
        """Gets the background_repeat of this CaptivePortalConfiguration.  # noqa: E501


        :return: The background_repeat of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: BackgroundRepeat
        """
        return self._background_repeat

    @background_repeat.setter
    def background_repeat(self, background_repeat):
        """Sets the background_repeat of this CaptivePortalConfiguration.


        :param background_repeat: The background_repeat of this CaptivePortalConfiguration.  # noqa: E501
        :type: BackgroundRepeat
        """

        self._background_repeat = background_repeat

    @property
    def radius_service_id(self):
        """Gets the radius_service_id of this CaptivePortalConfiguration.  # noqa: E501


        :return: The radius_service_id of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._radius_service_id

    @radius_service_id.setter
    def radius_service_id(self, radius_service_id):
        """Sets the radius_service_id of this CaptivePortalConfiguration.


        :param radius_service_id: The radius_service_id of this CaptivePortalConfiguration.  # noqa: E501
        :type: int
        """

        self._radius_service_id = radius_service_id

    @property
    def expiry_type(self):
        """Gets the expiry_type of this CaptivePortalConfiguration.  # noqa: E501


        :return: The expiry_type of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: SessionExpiryType
        """
        return self._expiry_type

    @expiry_type.setter
    def expiry_type(self, expiry_type):
        """Sets the expiry_type of this CaptivePortalConfiguration.


        :param expiry_type: The expiry_type of this CaptivePortalConfiguration.  # noqa: E501
        :type: SessionExpiryType
        """

        self._expiry_type = expiry_type

    @property
    def user_list(self):
        """Gets the user_list of this CaptivePortalConfiguration.  # noqa: E501


        :return: The user_list of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: list[TimedAccessUserRecord]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this CaptivePortalConfiguration.


        :param user_list: The user_list of this CaptivePortalConfiguration.  # noqa: E501
        :type: list[TimedAccessUserRecord]
        """

        self._user_list = user_list

    @property
    def mac_allow_list(self):
        """Gets the mac_allow_list of this CaptivePortalConfiguration.  # noqa: E501


        :return: The mac_allow_list of this CaptivePortalConfiguration.  # noqa: E501
        :rtype: list[MacAllowlistRecord]
        """
        return self._mac_allow_list

    @mac_allow_list.setter
    def mac_allow_list(self, mac_allow_list):
        """Sets the mac_allow_list of this CaptivePortalConfiguration.


        :param mac_allow_list: The mac_allow_list of this CaptivePortalConfiguration.  # noqa: E501
        :type: list[MacAllowlistRecord]
        """

        self._mac_allow_list = mac_allow_list

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
        if issubclass(CaptivePortalConfiguration, dict):
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
        if not isinstance(other, CaptivePortalConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
