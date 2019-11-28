# DJI / Ryze Tello drone control using MQTT

Control a DJI / Ryze Tello drone using MQTT messages.

This program needs to be run on a device that is connected to the Tello's
WiFi network.

For testing, a Raspberry Pi has been used with a WiFi connection to the
Tella and a wired Ethernet connection to the rest of the network, including
an MQTT broker.


## Dependencies
```
$ pip install tellopy
$ pip install paho_mqtt
```

## Setup

Install the dependencies.

Configure the address of the MQTT broker by editing tello_mqtt.py.

Configure the device to connect to the Tello's WiFi, which is an
unprotected network. This can usually be done by editing the file
"/etc/wpa_supplicant/wpa_supplicant.conf" and putting in an entry
similar to:
```
network={
    ssid="TELLO-58D7CD"
    key_mgmt=NONE
}
```

Substitute the SSID for your Tello.

Turn on the Tello, and wait for your device to connect and receive
an IP address. You can watch this process using something like:
```
watch ifconfig wlan0
```

Run the client:
```
$ ./tello_mqtt.py
```

Send commands to the MQTT broker. This can be done using the Mosquitto
example clients on the command line, like:
```
mosquitto_pub -t "device/tello/cmnd" -m "takeoff"
```

Currently implemented commands are:
 * takeoff
 * land
 * flip_forwards
 * flip_back

