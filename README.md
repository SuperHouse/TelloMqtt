# DJI / Ryze Tello drone control using MQTT

By Jonathan Oxer <jon@oxer.com.au>

Control a DJI / Ryze Tello drone using MQTT messages.

This program needs to be run on a device that is connected to the Tello's
WiFi network, and ALSO has access to an MQTT broker.

Testing has been done with a Raspberry Pi with a WiFi connection to the
Tello and a wired Ethernet connection to the rest of the network, including
an MQTT broker. You can also run the broker directly on your device if you
prefer.

## Setup

Requires Python3.

Install the required libraries:
```
$ pip install tellopy
$ pip install paho-mqtt
```

Configure the address of your MQTT broker by editing tello_mqtt.py.

Configure your device to connect to the Tello's WiFi, which is an
unprotected network. On Linux systems including Raspbian this can be
done by editing the file
"/etc/wpa_supplicant/wpa_supplicant.conf" and creating an entry
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

Once you see that your device has been assigned an IP address, you
know it has connected to the Tello.

Press CTL-C to end the "watch" command.

Run the TelloMqtt client:
```
$ ./tello_mqtt.py
```

Send commands to the MQTT broker. This can be done using the Mosquitto
command line client, like:
```
mosquitto_pub -t "device/tello/cmnd" -m "takeoff"
```

Currently implemented commands are:
 * takeoff
 * land
 * flip_forward
 * flip_back
 * flip_right
 * flip_left
 * flip_forwardleft
 * flip_backleft
 * flip_forwardright
 * flip_backright

 These commands are trivial wrappers for the TelloPy API so you can easily
 extend them by adding more API calls.

 Commands that require an argument or that return a value currently
 don't work.
