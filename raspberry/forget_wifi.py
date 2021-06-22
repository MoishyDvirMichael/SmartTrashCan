import os


def delete_data():
    init_data = '{"uid": "", "wifi": []}'
    command = "sudo echo '" + init_data + "' > /home/pi/Documents/SmartTrashCan/raspberry/data.json"
    os.system(command)


def forget_wifi():
    config = 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\ncountry=IL'
    command = "sudo echo '" + config + "' > /etc/wpa_supplicant/wpa_supplicant.conf"
    os.system(command)


def refresh():
    command = "wpa_cli -i wlan0 reconfigure"
    os.system(command)

if __name__ == '__main__':
    delete_data()
    forget_wifi()
    refresh()