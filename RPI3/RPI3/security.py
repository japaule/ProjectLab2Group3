#######################################################################
# security.py - Monitors a Mosquitto MQTT queue for security events
# from an array of secufity sensors, detects critical changes in those
# sensor values, and injects alarms into an io.adafruit.com queue.
# 
# Note: The hardware to do this is already developed (Feather Huzzah
# ESP8266 with NodeCMU), along with the Lua software to run on
# the ESP8266. The next development steps are:
# - write this python program
# - write the If This Then That interface to do notifications
#
# Note two: The implementation uses normally-closed reed switches
# from China. If you use normally open switches, you'll have to
# edit this code to invert the tests for the values coming from
# the sensors.
# 
# Philip R. Moyer
# Adafruit
# May 2016
#
# This code is released under a BSD liense and is in the public domain.
# Any redistribution must include the above header.
#######################################################################

########################
# Libraries
########################

import os
import string
import paho.mqtt.client as mqtt
import Adafruit_IO
import time


########################
# Globals
########################

# -- Change these as needed for your installatin --

localBroker = "192.168.1.93"		# Local MQTT broker
localPort = 1883			# Local MQTT port
localUser = "MQTT_user"			# Local MQTT user
localPass = "Password"			# Local MQTT password
localTopic = "/security"		# Local MQTT topic to monitor
localTimeOut = 120			# Local MQTT session timeout

adafruitUser = "YOUR_ADAFRUIT_IO_USERID"		# Adafruit.IO user ID
adafruitKey = "YOUR_ADAFRUIT_IO_KEY"	# Adafruit.IO user key
adafruitTopic = "alarms"		# Adafruit.IO alarm topic

# -- You should not need to change anything below this line --

sensorList = {}				# List of sensor objects


########################
# Classes and Methods
########################

class sensor():
	def __init__(self):
		self.name = ""		# Name of sensor in MQTT
		self.humanName = ""	# Human-meaningful name (e.g., "front door")
		self.lastSeen = 0	# Number of seconds since the sensor was last seen
		self.state = "unknown"	# State of the object: unknown, open, or closed

	def setState(self, newstate):
		self.state = newState

	def getState(self):
		return self.state

	def resetHeartbeat(self):
		self.lastSeen = 0

	def setname(self, newName, humanName):
		self.name = newName
		self.humanName = humanName

	def getname(self):
		return self.humanName

	def checkState(self, newState):
		if ("unknown" == self.state):
			self.state = newState
			return 0
		else:
			if (newState != self.state):
				self.state = newState
				if ("closed" == self.state):
					return -1
				else:
					return 1
		return 0
		

class sensorList():
	def __init__(self):
		self.sensorList = {}

	def addSensor(self, sensorName, humanName):
		self.sensorList[sensorName] = sensor()
		self.sensorList[sensorName].setname(sensorName, humanName)

	def getSensorName(self, sensorID):
		return self.sensorList[sensorID].getname()

	def sensorState(self, sensorID, monitorState):
		rv = self.sensorList[sensorID].checkState(monitorState)
		if (0 != rv):
			# State changed!
			if (0 > rv):
				outBuf = "INFO "+self.getSensorName(sensorID)+" "+monitorState
				print(outBuf)
			else:
				outBuf = "ALARM "+self.getSensorName(sensorID)+" "+monitorState
				print(outBuf)
				print("Initiating connection to Adafruit.IO")
				AIOclient = Adafruit_IO.MQTTClient(adafruitUser, adafruitKey)
				print("Setting callbacks for Adafruit.IO")
				AIOclient.on_connect = AIOconnected
				AIOclient.on_disconnect = AIOdisconnected
				AIOclient.on_message = AIOmessage
				print("Connecting to Adafruit.IO")
				AIOclient.connect()
				time.sleep(5)
				print("Publishing outBuf")
				# AIOclient.publish("alarms", outBuf)
				AIOclient.publish("alarms", outBuf)
				print("Disconnecting")
				AIOclient.disconnect()


########################
# Functions
########################

# Callback functions for Adafruit.IO connections
def AIOconnected(client):
	# client.subscribe('alarms')
	print("Connected to Adafruit.IO")

def AIOdisconnected(client):
	print("adafruit.io client disconnected!")

def AIOmessage(client, feed_id, payload):
	print("adafruit.io received ", payload)


# returnState takes a numeric voltage value from the sensor and
# returns the state of the monitored device. With a voltage divider
# that uses a 1M ohm R1 and a 470K ohm R2, the "closed" state returns
# 1024 and the open state returns between 1 and 40.

def returnState(inVal):
	if (1000 < inVal):
		return "closed"
	if (100 > inVal):
		return "open"
	else:
		return "unknown"


########################
# Main
########################

if "__main__" == __name__:
	# Set timer

	sensList = sensorList()
	sensList.addSensor("security_001", "front door")

	# The callback for when the client receives a CONNACK response from the server.
	def on_connect(client, userdata, flags, rc):
		print("Connected with result code "+str(rc))

		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		client.subscribe("/security")

	# The callback for when a PUBLISH message is received from the server.
	def on_message(client, userdata, msg):
		(sensorID, sensorVoltage) = string.split(msg.payload)
		sensorVoltage = string.atoi(sensorVoltage)
		sensorName = sensList.getSensorName(sensorID)
		sensList.sensorState(sensorID, returnState(sensorVoltage))
		# print(sensorName+" "+returnState(sensorVoltage))

	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect(localBroker, localPort, localTimeOut)

	# Blocking call that processes network traffic, dispatches callbacks and
	# handles reconnecting.
	# Other loop*() functions are available that give a threaded interface and a
	# manual interface.
	client.loop_forever()

	quit()