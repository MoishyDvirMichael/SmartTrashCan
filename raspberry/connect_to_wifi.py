import os
import time
import http.client as httplib

class ConnectToWifi:
    @classmethod
    def is_connected(cls):
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False

    @classmethod
    def connect(cls, name, password):
        createNewConnection(name, name, password)
        connect(name, name)

    @classmethod
    def try_old_connection(cls, previous_networks: list):
        try:
            if cls.is_connected():
                return True
            for previous_network in previous_networks:
                print(f'Trying to connect to {previous_network["name"]}')
                cls.connect(previous_network['name'], previous_network['password'])
                time.sleep(3)
                if cls.is_connected():
                    print(f'Successing to connect to {previous_network["name"]}')
                    return True
                print(f'Failing to connect to {previous_network["name"]}')
            return False
        except:
            return False

def connect(name, SSID):
	command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
	os.system(command)

def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\"wifi.xml\""+" interface=Wi-Fi"
    with open("wifi.xml", 'w') as file:
        file.write(config)
    os.system(command)
