import pytest
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)

if 'cloudsdk' not in sys.path:
    sys.path.append(f'../libs/cloudsdk')
if 'apnos' not in sys.path:
    sys.path.append(f'../libs/apnos')
if 'testrails' not in sys.path:
    sys.path.append(f'../libs/testrails')

from cloudsdk import ProfileUtility
from configuration_data import TEST_CASES


class TestProfileCleanup(object):

    @pytest.mark.hard_cleanup
    def test_profile_hard_cleanup(self, cleanup_cloud_profiles):
        # (cleanup_cloud_profiles)
        assert True

    @pytest.mark.sanity_cleanup
    @pytest.mark.run(order=5)
    @pytest.mark.bridge
    @pytest.mark.nat
    @pytest.mark.vlan
    @pytest.mark.fiveg
    @pytest.mark.wpa
    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    @pytest.mark.wpa2_enterprise
    def test_profile_cleanup(self, setup_profile_data, instantiate_profile, testrun_session):
        print("6")
        try:
            instantiate_profile.delete_profile_by_name(profile_name="Sanity-ecw5410-BRIDGE")
            instantiate_profile.delete_profile_by_name(profile_name="Sanity-" + testrun_session + "-NAT")
            instantiate_profile.delete_profile_by_name(profile_name="Sanity-" + testrun_session + "-VLAN")
            for i in setup_profile_data:
                for j in setup_profile_data[i]:
                    for k in setup_profile_data[i][j]:
                        instantiate_profile.delete_profile_by_name(
                            profile_name=setup_profile_data[i][j][k]['profile_name'])
            instantiate_profile.delete_profile_by_name(profile_name=testrun_session + "-RADIUS-Sanity")

            status = True
        except Exception as e:
            print(e)
            status = False
        assert status


@pytest.mark.run(order=6)
@pytest.mark.bridge
@pytest.mark.nat
@pytest.mark.vlan
@pytest.mark.fiveg
@pytest.mark.wpa
@pytest.mark.twog
@pytest.mark.wpa2_personal
@pytest.mark.wpa2_enterprise
class TestRfProfile(object):

    @pytest.mark.rf
    def test_radius_profile_creation(self, set_rf_profile):
        print("7")
        profile_data = set_rf_profile
        if profile_data:
            PASS = True
        else:
            PASS = False
        assert PASS


@pytest.mark.run(order=7)
@pytest.mark.bridge
@pytest.mark.nat
@pytest.mark.vlan
@pytest.mark.wpa2_enterprise
@pytest.mark.twog
@pytest.mark.fiveg
class TestRadiusProfile(object):

    @pytest.mark.radius
    def test_radius_profile_creation(self, instantiate_profile, create_radius_profile, testrun_session, instantiate_testrail, instantiate_project):
        print("8")
        profile_data = create_radius_profile
        if profile_data._name == testrun_session + "-RADIUS-Sanity":
            instantiate_testrail.update_testrail(case_id=TEST_CASES["radius_profile"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='RADIUS profile created successfully')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["radius_profile"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='Failed to create RADIUS profile')
            PASS = False
        assert PASS


@pytest.mark.run(order=8)
@pytest.mark.ssid
@pytest.mark.bridge
class TestProfilesBridge(object):

    def test_reset_profile(self, reset_profile):
        assert reset_profile

    @pytest.mark.fiveg
    @pytest.mark.wpa
    def test_ssid_wpa_5g(self, instantiate_profile, create_wpa_ssid_5g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_5g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA SSID create failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa
    def test_ssid_wpa_2g(self, instantiate_profile, create_wpa_ssid_2g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_2g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA SSID create failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_2g(self, instantiate_profile, create_wpa2_p_ssid_2g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_2g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 PERSONAL SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 PERSONAL SSID create failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_5g(self, instantiate_profile, create_wpa2_p_ssid_5g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_5g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 PERSONAL SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 PERSONAL SSID create failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_2g(self, instantiate_profile, create_wpa2_e_ssid_2g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_2g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 Enterprise SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 Enterprise SSID create failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_5g(self, instantiate_profile, create_wpa2_e_ssid_5g_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_5g_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 Enterprise SSID created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 Enterprise SSID create failed - bridge mode')
            PASS = False
        assert PASS


@pytest.mark.equipment_ap
class TestEquipmentAPProfile(object):

    @pytest.mark.run(order=9)
    @pytest.mark.bridge
    @pytest.mark.fiveg
    @pytest.mark.wpa
    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    @pytest.mark.wpa2_enterprise
    def test_equipment_ap_profile_bridge_mode(self, instantiate_profile, create_ap_profile_bridge, instantiate_testrail, instantiate_project):
        profile_data = create_ap_profile_bridge
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_bridge"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='EQUIPMENT AP PROFILE created successfully - bridge mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_bridge"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='EQUIPMENT AP PROFILE CREATION Failed - bridge mode')
            PASS = False
        assert PASS

    @pytest.mark.run(order=15)
    @pytest.mark.nat
    @pytest.mark.fiveg
    @pytest.mark.wpa
    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    @pytest.mark.wpa2_enterprise
    def test_equipment_ap_profile_nat_mode(self, create_ap_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_ap_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='EQUIPMENT AP PROFILE CREATION successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='EQUIPMENT AP PROFILE CREATION Failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.run(order=21)
    @pytest.mark.vlan
    @pytest.mark.fiveg
    @pytest.mark.wpa
    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    @pytest.mark.wpa2_enterprise
    def test_equipment_ap_profile_vlan_mode(self, create_ap_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_ap_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='EQUIPMENT AP PROFILE CREATION successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ap_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='EQUIPMENT AP PROFILE CREATION failed - vlan mode')
            PASS = False
        assert PASS


@pytest.mark.run(order=14)
@pytest.mark.ssid
@pytest.mark.nat
class TestProfilesNAT(object):

    def test_reset_profile(self, reset_profile):
        assert reset_profile

    @pytest.mark.fiveg
    @pytest.mark.wpa
    def test_ssid_wpa_5g(self, instantiate_profile, create_wpa_ssid_5g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_5g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA SSID create failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa
    def test_ssid_wpa_2g(self, instantiate_profile, create_wpa_ssid_2g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_2g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA SSID create failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_2g(self, instantiate_profile, create_wpa2_p_ssid_2g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_2g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 PERSONAL SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 PERSONAL SSID create failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_5g(self, instantiate_profile, create_wpa2_p_ssid_5g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_5g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 PERSONAL SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 PERSONAL SSID create failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_2g(self, instantiate_profile, create_wpa2_e_ssid_2g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_2g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 Enterprise SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 Enterprise SSID create failed - nat mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_5g(self, instantiate_profile, create_wpa2_e_ssid_5g_profile_nat, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_5g_profile_nat
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_nat"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 Enterprise SSID created successfully - nat mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_nat"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 Enterprise SSID create failed - nat mode')
            PASS = False
        assert PASS


@pytest.mark.run(order=20)
@pytest.mark.ssid
@pytest.mark.vlan
class TestProfilesVLAN(object):

    def test_reset_profile(self, reset_profile):
        assert reset_profile

    @pytest.mark.fiveg
    @pytest.mark.wpa
    def test_ssid_wpa_5g(self, instantiate_profile, create_wpa_ssid_5g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_5g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA SSID create failed - vlan mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa
    def test_ssid_wpa_2g(self, instantiate_profile, create_wpa_ssid_2g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa_ssid_2g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA SSID create failed - vlan mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_2g(self, instantiate_profile, create_wpa2_p_ssid_2g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_2g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 PERSONAL SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_wpa2_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 PERSONAL SSID create failed - vlan mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_personal
    def test_ssid_wpa2_personal_5g(self, instantiate_profile, create_wpa2_p_ssid_5g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_p_ssid_5g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 PERSONAL SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_wpa2_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 PERSONAL SSID create failed - vlan mode')
            PASS = False
        assert PASS

    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_2g(self, instantiate_profile, create_wpa2_e_ssid_2g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_2g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='2G WPA2 Enterprise SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_2g_eap_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='2G WPA2 Enterprise SSID create failed - vlan mode')
            PASS = False
        assert PASS

    @pytest.mark.fiveg
    @pytest.mark.wpa2_enterprise
    def test_ssid_wpa2_enterprise_5g(self, instantiate_profile, create_wpa2_e_ssid_5g_profile_vlan, instantiate_testrail, instantiate_project):
        profile_data = create_wpa2_e_ssid_5g_profile_vlan
        if profile_data:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_vlan"], run_id=instantiate_project,
                                                 status_id=1,
                                                 msg='5G WPA2 Enterprise SSID created successfully - vlan mode')
            PASS = True
        else:
            instantiate_testrail.update_testrail(case_id=TEST_CASES["ssid_5g_eap_vlan"], run_id=instantiate_project,
                                                 status_id=5,
                                                 msg='5G WPA2 Enterprise SSID create failed - vlan mode')
            PASS = False
        assert PASS

