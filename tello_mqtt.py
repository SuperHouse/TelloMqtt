#!/usr/bin/env python3
# pip3 install paho-mqtt
# pip3 install tellopy

import paho.mqtt.client as mqtt
import tellopy
import time

broker_address="192.168.0.96"

def mqtt_on_connect(client, userdata, flags, rc):
     logging.info("Connected flags"+str(flags)+"result code "\
     +str(rc)+"client1_id ")
     client.connected_flag=True

def mqtt_on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    print(message.payload.decode("utf-8"))
    if message.payload.decode("utf-8") == 'takeoff':
        print("Takeoff!")
        tello_takeoff()
    if message.payload.decode("utf-8") == 'land':
        print("Land!")
        tello_land()
    if message.payload.decode("utf-8") == 'flip_forward':
        print("Flip Forward")
        tello_flip_forward()
    if message.payload.decode("utf-8") == 'flip_back':
        print("Flip Back")
        tello_flip_back()


def tello_handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

def tello_takeoff():
    drone.takeoff()

def tello_land():
    drone.land()

def tello_flip_forward():
    drone.flip_forward()

def tello_flip_back():
    drone.flip_back()

print("Creating MQTT client instance")
client =mqtt.Client("Tello")
client.on_connect= mqtt_on_connect
client.on_message= mqtt_on_message

print("Connecting to MQTT broker")
client.connect(broker_address)

print ("Subscribing to topic 'device/tello/cmnd'")
client.subscribe("device/tello/cmnd")

print("Creating Tello client instance")
drone = tellopy.Tello()

try:
    drone.subscribe(drone.EVENT_FLIGHT_DATA, tello_handler)
    print("Connecting to Tello")
    drone.connect()
    drone.wait_for_connection(60.0)
    print("Finished")
except Exception as ex:
    print(ex)
finally:
    drone.quit()

client.loop_forever()

