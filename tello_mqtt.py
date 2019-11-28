#!/usr/bin/env python

import paho.mqtt.client as mqtt

from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())

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
    if message.payload.decode("utf-8") == 'command':
        print("Command mode")
        tello_command()
    if message.payload.decode("utf-8") == 'takeoff':
        print("Takeoff!")
        tello_takeoff()
    if message.payload.decode("utf-8") == 'land':
        print("Land!")
        tello_land()
    if message.payload.decode("utf-8") == 'flip_forward':
        print("Flip forward")
        tello_flip_forward()
    if message.payload.decode("utf-8") == 'flip_back':
        print("Flip back")
        tello_flip_back()
    if message.payload.decode("utf-8") == 'throw_and_go':
        print("Throw and go")
        tello_throw_and_go()
    if message.payload.decode("utf-8") == 'get_alt_limit':
        print("Get alt Limit")
        tello_get_alt_limit()
    if message.payload.decode("utf-8") == 'get_att_limit':
        print("Get att limit")
        tello_get_att_limit()
    if message.payload.decode("utf-8") == 'get_low_bat_threshold':
        print("Get low battery threshold")
        tello_get_low_bat_threshold()
    if message.payload.decode("utf-8") == 'take_picture':
        print("Take picture")
        tello_take_picture()
    if message.payload.decode("utf-8") == 'flip_right':
        print("Flip right")
        tello_flip_right()
    if message.payload.decode("utf-8") == 'flip_left':
        print("Flip left")
        tello_flip_left()
    if message.payload.decode("utf-8") == 'flip_forwardleft':
        print("Flip forward left")
        tello_flip_forwardleft()
    if message.payload.decode("utf-8") == 'flip_backleft':
        print("Flip back left")
        tello_flip_backleft()
    if message.payload.decode("utf-8") == 'flip_forwardright':
        print("Flip forward right")
        tello_flip_forwardright()
    if message.payload.decode("utf-8") == 'flip_backright':
        print("Flip back right")
        tello_flip_backright()

def mqtt_on_publish(client, userdata, result):
    print("Data published \n")
    pass

def tello_handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

def tello_takeoff():
    tello.takeoff()

def tello_land():
    tello.land()

def tello_flip_forward():
    drone.flip_forward()

def tello_flip_back():
    drone.flip_back()

def tello_throw_and_go():
    drone.throw_and_go()

def tello_get_alt_limit():
    drone.get_alt_limit()

def tello_get_att_limit():
    drone.get_att_limit()

def tello_get_low_bat_threshold():
    drone.get_low_bat_threshold()

def tello_take_picture():
    drone.take_picture()

def tello_flip_right():
    drone.flip_right()

def tello_flip_left():
    drone.flip_left()

def tello_flip_forwardleft():
    drone.flip_forwardleft()

def tello_flip_backleft():
    drone.flip_backleft()

def tello_flip_forwardright():
    drone.flip_forwardright()

def tello_flip_backright():
    drone.flip_backright()


print("Creating MQTT client instance")
client =mqtt.Client("Tello")
client.on_connect= mqtt_on_connect
client.on_message= mqtt_on_message
client.on_publish= mqtt_on_publish

client1 =mqtt.Client("Tello1")

print("Connecting to MQTT broker")
client.connect(broker_address)
client1.connect(broker_address)

print ("Subscribing to topic 'device/tello/cmnd'")
client.subscribe("device/tello/cmnd")

print("Creating Tello client instance")
dronee = Tello()

while 1:
    client.loop(0.1)


