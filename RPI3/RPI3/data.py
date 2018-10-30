#File used to communicate with esp8266 to gather json location data
# REV 1.1


import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
########################################
broker_address="192.168.1.10"
print("creating new instance")
client = mqtt.Client("P1") 
client.on_message=on_message 
print("connecting to broker")
client.connect(broker_address) 
client.loop_start() 
client.subscribe("Rover1/#")



client.publish("Rover1/M1",300)
time.sleep(.9)
client.publish("Rover1/M2",300)
time.sleep(.8)

