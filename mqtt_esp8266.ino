#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.

const char* ssid = "ATT678F8hN";
const char* password = "8jvk4m?nk#zh";
const char* mqtt_server = "192.168.1.73";


WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("Test" , "Connected");
      // ... and resubscribe
      client.subscribe("inTopic");
      client.subscribe("cole");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void getserial(){
  String topic;
  String temp;
  String message= "";
  while (Serial.available()) {
    message = Serial.readString();
  }
    
  if(message[0] == '['){
    message.remove(0,1);
    int i = 0;
    while(message[i] != ']' && i <= message.length()){
      i++;
    }
        temp = message;
        message.remove(i,message.length() - i);
        topic = message;
        message = temp;
        message.remove(i,2);
        message.remove(message.length() -1, 1);
        message.remove(0, i);
        char top[topic.length()]; 
        topic.toCharArray(top, topic.length()+1);
        char msg[message.length()]; 
        message.toCharArray(msg, message.length()+1);
        client.publish(top, msg);
  }
  if(message[0] == '*'){
      message.remove(0,2);
      message.remove(message.length()-1, 1);

      char msg[message.length()]; 
      message.toCharArray(msg, message.length()+1);
      client.subscribe(msg);
      Serial.print("Subscribed to ");
      Serial.println(msg);
    }
}




void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  getserial();
}
