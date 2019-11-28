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
