# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import ipaddress
import wifi
import time
import socketpool


wifi.radio.start_ap("GreyMan", "12345678", channel=2)
print("created")


def storage_mode():
    import storage
    storage.remount("/", False)
    os.remove("/boot.py")

def connect_wifi():
    print("Connecting to WiFi")

    #  connect to your SSID
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

    print("Connected to WiFi")

    pool = socketpool.SocketPool(wifi.radio)

    #  prints MAC address to REPL
    print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

    #  prints IP address to REPL
    print("My IP address is", wifi.radio.ipv4_address)

    #  pings Google
    ipv4 = ipaddress.ip_address("8.8.4.4")
    print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))

connect_wifi()