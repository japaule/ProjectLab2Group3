#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
 
const char* ssid = "TTUSwarmField";
const char* password = "yourNetworkPassword";
 
void setup () {
 
  Serial.begin(115200);
  WiFi.begin(ssid);
 //User knows when to wait for wifi connection
  while (WiFi.status() != WL_CONNECTED) {
 
    delay(1000);
    Serial.print("Connecting..");
 
  }
 
}
 //this part of the code is for when the WIFI has been connected
//It declares to use the URL HTTP for the data
//then it defines the IP address of Prof. Johnston's network were pulling from
//if data is retrieved the connection closes but asks for more information every 30 seconds
void loop() {
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    HTTPClient http;  //Declare an object of class HTTPClient
 
    http.begin("http://172.16.0.1:8001/FieldData/GetData");  //Specify request destination
    int httpCode = http.GET();                                                                  //Send the request
 
    if (httpCode > 0) { //Check the returning code
 
      String payload = http.getString();   //Get the request response payload
      Serial.println(payload);                     //Print the response payload
 
    }
 
    http.end();   //Close connection
 
  }
 
  delay(500);    //Send a request every 30 seconds
 
}
