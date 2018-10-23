#include <SoftwareSerial.h>
//#include <AltSoftSerial.h>
#include <WickedMotorShield.h>

SoftwareSerial mySerial(3,10);

Wicked_DCMotor m1(M1);
Wicked_DCMotor m2(M2);
Wicked_DCMotor m3(M3);

double w1=0,w2=0,w3=0;

String info;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(57600);
  
  mySerial.begin(9600);
  mySerial.setTimeout(3);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
  m1.setBrake(BRAKE_OFF);
  m2.setBrake(BRAKE_OFF);
  m3.setBrake(BRAKE_OFF);

  delay(2000);

  mySerial.println("*[Rover1]");
  delay(500);
  mySerial.println("[Rover1][0-0-0]");
  delay(500);
  
}

void motors(){

  
  boolean w1_ccw = w1 < 0 ? true : false;
  boolean w2_ccw = w2 < 0 ? true : false;
  boolean w3_ccw = w3 < 0 ? true : false;
  byte w1_speed = (byte) map(abs(w1), 0, 600, 0, 255);
  byte w2_speed = (byte) map(abs(w2), 0, 600, 0, 255);
  byte w3_speed = (byte) map(abs(w3), 0, 600, 0, 255);
  m1.setDirection(w1_ccw ? DIR_CCW : DIR_CW);
  m2.setDirection(w2_ccw ? DIR_CCW : DIR_CW);
  m3.setDirection(w3_ccw ? DIR_CCW : DIR_CW);
 
  m1.setSpeed(w1_speed);
  m2.setSpeed(w2_speed);
  m3.setSpeed(w3_speed);
  
}


void loop() { // run over and over
  if (mySerial.available()) {
    //Serial.print((char)mySerial.read());
    info = mySerial.readStringUntil('/n');
    
    Serial.println(info);
    if(info[0] == '['){
      String temp;
      String topic;
      info.remove(0,1);
      info.remove(info.length()-1,1);
      int i = 0;
       while(info[i] != ']' && i <= info.length()){
        i++;
      }
      info.remove(i,2);
      info.remove(info.length() -1, 1);
      info.remove(0, i);
    
      for(i = 0; info[i]!='_';i++){}
      temp = info;
      info.remove(i, info.length()-i); 
      w1 = info.toInt();
      info = temp;
      info.remove(0,i+1);
    
      for(i = 0; info[i]!='_';i++){}
      temp = info;
      info.remove(i, info.length()-i);
      w2 = info.toInt();
      info = temp;
      info.remove(0,i+1);
    
      info.remove(info.length()-1, 1);
      w3 = info.toInt();
      motors();
      info ="";
    }
  }
  
  
  
  if (Serial.available()) {
    mySerial.print(Serial.read());
  }
}
    

