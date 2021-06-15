import os
import time
import http.client as httplib


class ConnectToWifi:
    
    highest_priority = 0
    
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
    def connect(cls, name, password=None):
        cls.highest_priority += 1
        createNewConnection(cls.highest_priority, name, password)
        refresh()

    @classmethod
    def try_reconnect(cls):
        try:
            if cls.is_connected():
                return True
            refresh()
            time.sleep(5)
            for i in range(1, 7):
                if cls.is_connected():
                    return True
                time.sleep(i)
            return False
        except:
            return False


def refresh():
	command = "wpa_cli -i wlan0 reconfigure"
	os.system(command)

def createNewConnection(priority, ssid, password=None):
    config = generate_unsucure_network_config(ssid, priority) if password == None or password == '' else generate_sucure_network_config(ssid, password, priority)
    command = "sudo echo '" + config + "' >> /etc/wpa_supplicant/wpa_supplicant.conf"
    os.system(command)

def generate_sucure_network_config(ssid, password, priority):
    return """
network={
	ssid=\"""" + ssid + """\"
	psk=\"""" + password + """\"
	priority=""" + str(priority) + """
}
"""

def generate_unsucure_network_config(ssid, priority):
    return """
network={
	ssid=\"""" + ssid + """\"
	priority=""" + str(priority) + """
	key_mgmt=NONE	
}
"""
