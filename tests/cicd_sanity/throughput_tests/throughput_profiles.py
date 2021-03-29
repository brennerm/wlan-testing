import os
import sys
import datetime
from datetime import date
import time
# Used to create SSID and AP profiles for throughput tests

if 'cicd_sanity' not in sys.path:
    sys.path.append('..')

import cloud_connect
from cloud_connect import CloudSDK


def main(fw_model, cloudSDK_url, cloud_type, customer_id, cloud_user, cloud_password, mode, ssid_psk, radius_profile, rf_profile, vlan, ssid_list):
    ssid_template = "../templates/ssid_profile_template.json"
    ap_template = "../templates/ap_profile_template.json"
    name = fw_model + " Automation_TPUT_" + mode

    if mode == 'nat':
        ssid_mode = "NAT"
    else:
        ssid_mode = "BRIDGE"

    bearer = CloudSDK.get_bearer(cloudSDK_url, cloud_type, cloud_user, cloud_password)

    # Profile Dictionary
    profile_list = []

    # Delete any existing profiles with the same name
    # Delete existing SSID profiles
    for key in ssid_list:
        existing_profile = CloudSDK.get_profile_by_name(cloudSDK_url, bearer, str(customer_id), str(ssid_list[key]))
        if not existing_profile:
            pass
        else:
            for x in existing_profile:
                CloudSDK.delete_profile(cloudSDK_url, bearer, str(x))
    # Delete existing AP profiles
    existing_ap_profile = CloudSDK.get_profile_by_name(cloudSDK_url, bearer, str(customer_id), str(name))
    if not existing_ap_profile:
        pass
    else:
        for x in existing_ap_profile:
            CloudSDK.delete_profile(cloudSDK_url, bearer, str(x))

    print(fw_model)
    # Create Profiles
    print(mode + " profile create..")
    fiveG_eap = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                             ssid_list["5g_eap"], customer_id,
                                             ssid_list["5g_eap"], None,
                                             radius_profile,
                                             "wpa2OnlyRadius", ssid_mode, vlan,
                                             ["is5GHzU", "is5GHz", "is5GHzL"])
    print("5G EAP:", fiveG_eap)
    profile_list.append(fiveG_eap)

    fiveG_wpa2 = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                              ssid_list["5g_wpa2"], customer_id,
                                              ssid_list["5g_wpa2"],
                                              ssid_psk,
                                              0, "wpa2OnlyPSK", ssid_mode, vlan,
                                              ["is5GHzU", "is5GHz", "is5GHzL"])
    print("5G WPA2:",fiveG_wpa2)
    profile_list.append(fiveG_wpa2)

    fiveG_wpa = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                             ssid_list["5g_wpa"], customer_id,
                                             ssid_list["5g_wpa"],
                                             ssid_psk,
                                             0, "wpaPSK", ssid_mode, vlan,
                                             ["is5GHzU", "is5GHz", "is5GHzL"])
    print("5G WPA:", fiveG_wpa)
    profile_list.append(fiveG_wpa)

    twoFourG_eap = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                                ssid_list["2g_eap"], customer_id,
                                                ssid_list["2g_eap"],
                                                None,
                                                radius_profile, "wpa2OnlyRadius", ssid_mode, vlan,
                                                ["is2dot4GHz"])
    print("2G EAP:", twoFourG_eap)
    profile_list.append(twoFourG_eap)
    twoFourG_wpa2 = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                                 ssid_list["2g_wpa2"], customer_id,
                                                 ssid_list["2g_wpa2"], ssid_psk,
                                                 0, "wpa2OnlyPSK", ssid_mode, vlan,
                                                 ["is2dot4GHz"])
    print("2G WPA2:", twoFourG_wpa2)
    profile_list.append(twoFourG_wpa2)

    twoFourG_wpa = CloudSDK.create_ssid_profile(cloudSDK_url, bearer, ssid_template,
                                                ssid_list["2g_wpa"], customer_id,
                                                ssid_list["2g_wpa"], ssid_psk,
                                                0, "wpaPSK", ssid_mode, vlan,
                                                ["is2dot4GHz"])
    print("2G WPA:", twoFourG_wpa)
    profile_list.append(twoFourG_wpa)

    child_profiles = [fiveG_eap, fiveG_wpa2, fiveG_wpa, twoFourG_eap, twoFourG_wpa2, twoFourG_wpa,
                      rf_profile]
    print(child_profiles)

    create_ap_profile = CloudSDK.create_ap_profile(cloudSDK_url, bearer, ap_template, name, customer_id, child_profiles)
    profile_list.append(create_ap_profile)
    ap_profile = create_ap_profile

    return profile_list, ap_profile
