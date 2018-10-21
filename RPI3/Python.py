import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
########################################
broker_address="192.168.1.2"
print("creating new instance")
client = mqtt.Client("P1") 
client.on_message=on_message 
print("connecting to broker")
client.connect(broker_address) 
client.loop_start() 
print("Subscribing to topic","test")
client.subscribe("test")
print("Publishing message to topic","test")
client.publish("test","OFF")
time.sleep(10) 
client.loop_stop() 
