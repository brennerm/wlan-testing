import csv
import sys
import time
import datetime
from datetime import date
import json
import os
import logging
import argparse
import importlib

if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit(1)

if 'cicd_sanity' not in sys.path:
    sys.path.append('..')

sys.path.append('../test_bed_info')

import unidirectional_throughput
import cloud_connect
from cloud_connect import CloudSDK
import throughput_profiles
import ap_connect

# Command Line Args
parser = argparse.ArgumentParser(description="Throughput Testing on APs")
parser.add_argument("-m", "--model", type=str, choices=['ea8300', 'ecw5410', 'ecw5211', 'ec420', "wf188n", "wf194c", "ex227", "ex447", "eap101", "eap102"],
                    help="AP model to be run")
parser.add_argument("-f", "--file", type=str, help="Test Info file name", default="../test_bed_info/test_info")
parser.add_argument("--skip_bridge", dest="skip_bridge", action='store_true', help="Skip Bridge testing")
parser.set_defaults(skip_bridge=False)
parser.add_argument("--skip_nat", dest="skip_nat", action='store_true', help="Skip NAT testing")
parser.set_defaults(skip_nat=False)
parser.add_argument("--skip_vlan", dest="skip_vlan", action='store_true', help="Skip VLAN testing")
parser.set_defaults(skip_vlan=False)
args = parser.parse_args()

# Import info for lab setup and APs under test
test_file = args.file
file = os.path.splitext(test_file)[0]
print(file)
if '/' in test_file:
    path, file = os.path.split(file)
    sys.path.append(path)
    test_info = importlib.import_module(file)
else:
    test_info = importlib.import_module(file)

#SSID modes to test
ssid_modes = []
if args.skip_bridge is not True:
    ssid_modes.append("bridge")
if args.skip_nat is not True:
    ssid_modes.append("nat")
if args.skip_vlan is not True:
    ssid_modes.append("vlan")

profile_info_dict = test_info.profile_info_dict
ap_models = test_info.ap_models
mimo_2dot4g = test_info.mimo_2dot4g
mimo_5g = test_info.mimo_5g
customer_id = test_info.customer_id
cloud_type = test_info.cloud_type

cloudSDK_url = test_info.cloudSDK_url
cloud_user = test_info.cloud_user
cloud_password = test_info.cloud_password

lanforge_ip = test_info.lanforge_ip
station = ["tput5000"]
runtime = 10
ssid_psk = "Connectus123$"
csv_path="tput-results/"
bridge_upstream_port = test_info.lanforge_bridge_port
nat_upstream_port = test_info.lanforge_bridge_port
vlan_upstream_port = test_info.lanforge_vlan_port

#EAP Credentials
identity = test_info.radius_info['eap_identity']
ttls_password = test_info.radius_info['eap_pwd']

#Logging Info
local_dir= test_info.sanity_log_dir
logger = logging.getLogger('Throughput_Test')
hdlr = logging.FileHandler(local_dir+"/Throughput_Testing.log")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput):
    #parse client_tput list returned from unidirectional_throughput
    udp_ds = client_tput[0].partition(": ")[2]
    udp_us = client_tput[1].partition(": ")[2]
    tcp_ds = client_tput[2].partition(": ")[2]
    tcp_us = client_tput[3].partition(": ")[2]
    # Find band for CSV ---> This code is not great, it SHOULD get that info from LANForge!
    if "5G" in ssid_name:
        frequency = "5 GHz"
    elif "2G" in ssid_name:
        frequency = "2.4 GHz"
    else:
        frequency = "Unknown"
    # Append row to top of CSV file
    row = [ap_model, firmware, frequency, mimo, security, mode, udp_ds, udp_us, tcp_ds, tcp_us]
    with open(csv_file, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines.insert(1, row)
    with open(csv_file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    readFile.close()
    writeFile.close()

print("--Start of Throughput Test--")
print("Testing SSID modes: ", ssid_modes)
logger.info('Start of Throughput Test')

#Import dictionaries for AP Info
equipment_ids = test_info.equipment_id_dict
if args.model is not None:
    model_id = args.model
    equipment_ids = {
        model_id: test_info.equipment_id_dict[model_id]
    }
    print("User requested test on equipment ID:", equipment_ids)

ap_firmware_dict = {}

for key in equipment_ids:
    logger.info("Running throughput test on " + key)

    # Get Bearer Token to make sure its valid (long tests can require re-auth)
    bearer = CloudSDK.get_bearer(cloudSDK_url, cloud_type, cloud_user, cloud_password)

    # Get Current AP Firmware
    equipment_id = test_info.equipment_id_dict[key]
    ap_fw = CloudSDK.ap_firmware(customer_id, equipment_id, cloudSDK_url, bearer)

    # If AP FW is not returned skip equipmentId
    if ap_fw == 'ERROR':
        print("Error reading AP FW from CloudSDK. Skipping Equipment")
        continue

    # Get AP model from FW to ensure it matches key
    fw_model = ap_fw.partition("-")[0]
    print('Current AP Firmware:', ap_fw)

    if str(fw_model) != str(key):
        print('AP model reported in FW version does not match key! Skipping equipment')
        logger.warning('AP model reported in FW version does not match key! Aborting test for this Equipment')
        continue

    # add current FW to dictionary
    ap_firmware_dict[key] = ap_fw

    # CSV results file directory for model
    path = csv_path + "/" + fw_model + "/"
    isdir = os.path.isdir(path)
    if not isdir:
        print("Creating directory for AP model results")
        os.mkdir(csv_path + "/" + fw_model)

    # create CSV file for test run
    today = str(date.today())
    csv_file = path + key + "_throughput_test_" + ap_fw + "_" + today + ".csv"
    headers = ['AP Type', 'Firmware', 'Radio', 'MIMO', 'Security', 'Mode', 'UDP Downstream (Mbps)',
               'UDP Upstream (Mbps)', 'TCP Downstream (Mbps)', 'TCP Upstream (Mbps)']
    with open(csv_file, "w") as file:
        create = csv.writer(file)
        create.writerow(headers)
        file.close()

    for mode in ssid_modes:
        print("Testing for " + mode + " SSIDs")
        logger.info("Starting " + mode + " SSID tput tests on " + key)

        # SSID list - this is hardcoded values based on mode and AP model for now <-- room for improvement
        # SSID list
        ssid_list = {
            "5g_eap": fw_model + "_5G_EAP_tput_" + mode,
            "5g_wpa2": fw_model + '_5G_WPA2_tput_' + mode,
            "5g_wpa": fw_model + '_5G_WPA_tput_' + mode,
            "2g_eap": fw_model + '_2G_EAP_tput_' + mode,
            "2g_wpa2": fw_model + '_2G_WPA2_tput_' + mode,
            "2g_wpa": fw_model + '_2G_WPA_tput_' + mode
        }
        print("SSID List: ", ssid_list)

        # Set VLAN for profiles
        if mode == "vlan":
            vlan = test_info.vlan
        else:
            vlan = 1

        # Create Profiles for Testing
        profiles = throughput_profiles.main(fw_model, cloudSDK_url, cloud_type, customer_id, cloud_user, cloud_password, mode, ssid_psk, test_info.radius_profile, test_info.rf_profile_wifi5, vlan, ssid_list)
        print("AP Profile: ",profiles[1])

        # Set Proper AP Profile for Tests
        test_profile_id = profiles[1]
        ap_profile = CloudSDK.set_ap_profile(equipment_id, test_profile_id, cloudSDK_url, bearer)
        # Wait for Profile Push
        print('-----------------PROFILE PUSH -------------------')
        time.sleep(180)

        # Check that AP profile has been properly applied to VIF State
        ap_ip = test_info.equipment_ip_dict[key]
        ap_username = test_info.ap_user
        ap_password = test_info.equipment_credentials_dict[key]
        ssid_state = ap_connect.get_vif_state(ap_ip, ap_username, ap_password)
        print("SSIDs in AP VIF State:", ssid_state)

        if set(ssid_list[k] for k in ssid_list) == set(ssid_state):
            print("SSIDs in Wifi_VIF_State Match AP Profile Config")
            pass
        else:
            print("VIF State not applied properly on AP. Aborting Test for", mode, "mode...")
            logger.warning("VIF State not applied properly on AP. Aborting Test for "+mode+" mode...")
            # Set AP to default profile to facilitate profile delete
            ap_profile = CloudSDK.set_ap_profile(equipment_id, 6, cloudSDK_url, bearer)
            time.sleep(5)
            # Delete profiles created for test
            for x in profiles[0]:
                delete_profile = CloudSDK.delete_profile(cloudSDK_url, bearer, str(x))
                if delete_profile == "SUCCESS":
                    print("profile", x, "delete successful")
                else:
                    print("Error deleting profile ", x)
            continue

        # Set port for LANForge
        if mode == "bridge":
            port = bridge_upstream_port
        if mode == "nat":
            port = nat_upstream_port
        if mode == "vlan":
            port = vlan_upstream_port

        # 5G WPA2 Enterprise UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        sta_list = station
        radio = test_info.lanforge_5g
        ssid_name = ssid_list["5g_eap"]
        security = "wpa2"
        eap_type = "TTLS"
        mimo = mimo_5g[fw_model]
        client_tput = unidirectional_throughput.eap_tput(sta_list, ssid_name, radio, security, eap_type, identity, ttls_password, lanforge_ip, port)
        print(fw_model, "5 GHz WPA2-EAP throughput:\n", client_tput)
        security = "wpa2-eap"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        #5G WPA2 UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        radio = test_info.lanforge_5g
        ssid_name = ssid_list["5g_wpa2"]
        security = "wpa2"
        mimo = mimo_5g[fw_model]
        client_tput = unidirectional_throughput.main(ap_model, firmware, radio, ssid_name, ssid_psk, security, station, runtime, lanforge_ip, port)
        print(fw_model, "5 GHz WPA2 throughput:\n",client_tput)
        security = "wpa2-psk"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        # 5G WPA UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        radio = test_info.lanforge_5g
        ssid_name = ssid_list["5g_wpa"]
        security = "wpa"
        mimo = mimo_5g[fw_model]
        client_tput = unidirectional_throughput.main(ap_model, firmware, radio, ssid_name, ssid_psk, security, station, runtime, lanforge_ip, port)
        print(fw_model, "5 GHz WPA throughput:\n",client_tput)
        security = "wpa-psk"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        # 2.4G WPA2 Enterprise UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        sta_list = station
        radio = test_info.lanforge_2dot4g
        ssid_name = ssid_list["2g_eap"]
        security = "wpa2"
        eap_type = "TTLS"
        mimo = mimo_2dot4g[fw_model]
        client_tput = unidirectional_throughput.eap_tput(sta_list, ssid_name, radio, security, eap_type, identity,
                                                         ttls_password, lanforge_ip, port)
        print(fw_model, "2.4 GHz WPA2-EAP throughput:\n", client_tput)
        security = "wpa2-eap"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        # 2.4G WPA2 UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        radio = test_info.lanforge_2dot4g
        ssid_name = ssid_list["2g_wpa2"]
        security = "wpa2"
        mimo = mimo_2dot4g[fw_model]
        client_tput = unidirectional_throughput.main(ap_model, firmware, radio, ssid_name, ssid_psk, security, station, runtime, lanforge_ip, port)
        print(fw_model, "2.4 GHz WPA2 throughput:\n",client_tput)
        security = "wpa2-psk"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        # 2.4G WPA UDP DS/US and TCP DS/US
        ap_model = fw_model
        firmware = ap_fw
        radio = test_info.lanforge_2dot4g
        ssid_name = ssid_list["2g_wpa"]
        security = "wpa"
        mimo = mimo_2dot4g[fw_model]
        client_tput = unidirectional_throughput.main(ap_model, firmware, radio, ssid_name, ssid_psk, security, station, runtime, lanforge_ip, port)
        print(fw_model, "2.4 GHz WPA throughput:\n", client_tput)
        security = "wpa-psk"
        throughput_csv(csv_file, ssid_name, ap_model, mimo, firmware, security, mode, client_tput)

        # Delete profiles created for test
        print("Cleaning up! Deleting created test profiles")
        # Set AP to use permanently available profile to allow for deletion
        print("Set AP to profile not created in test")
        bearer = CloudSDK.get_bearer(cloudSDK_url, cloud_type, cloud_user, cloud_password)
        ap_profile = CloudSDK.set_ap_profile(equipment_id, 6, cloudSDK_url, bearer)
        time.sleep(5)
        # Delete SSID profiles
        for x in profiles[0]:
            delete_profile = CloudSDK.delete_profile(cloudSDK_url, bearer, str(x))
            if delete_profile == "SUCCESS":
                print("profile", x, "delete successful")
            else:
                print("Error deleting profile ", x)

    # If file has only header line, delete it
    with open(csv_file, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        row_count = len(lines)

    if row_count <= 1:
        os.remove(csv_file)
        print("CSV file has no results, deleting")
        logger.warning("CSV file forv"+key+"has no results...deleting")
        file.close()

    else:
        print("Saving CSVFile for ", key)
        file.close()

    print("--Throughput Test for "+key+" Complete")
print("-- Throughput Testing Complete --")
