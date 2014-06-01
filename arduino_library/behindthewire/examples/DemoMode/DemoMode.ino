/* This sketch is not yet finished, it is just meant to be a simple demo
 * of blinking lights and moving things to attract the visitors.
 * Feel free to add to it.
 */
#include <BehindTheWire.h>
#include <Servo.h>

int ButtonLeft = 0;
int ButtonRight = 0;
int power = 0;
int angle = 0;
BehindTheWire functions;
boolean angleUp = true;

void setup() {

  pinMode(RedLight,OUTPUT);             // Make the red Light an Output
  pinMode(WhiteLight,OUTPUT);           // Make the white Light an Output
  pinMode(GreenLight,OUTPUT);           // Make the green Light an Output
  pinMode(LeftButton,INPUT);            // Make the On/Left Button an Input
  pinMode(RightButton,INPUT);           // Make the Off/Right Button an Input
  pinMode(EngineLeft,OUTPUT);           // Make the Left Engine an Output
  pinMode(EngineRight,OUTPUT);          // Make the Left Engine an Output

  functions.rudderPrepare();            // Set up the rudder
 
}

void loop() {
  
  lightShow();
  
  functions.rudderSetPosition(angle);

  
  if(angle>45) {
    angleUp = false;
    angle = 45;
  } else if (angle<-45) {
    angleUp = true;
    angle = -45;
  }
  if(angleUp == true) {
    angle += 5;
  } else {
    angle -= 5; 
  }

  delay(1000);

}

void lightShow() {
  
  digitalWrite(RedLight,ON);
  delay(500);
  digitalWrite(WhiteLight,ON);
  delay(500);
  digitalWrite(GreenLight,ON);
  delay(500);
  digitalWrite(RedLight,OFF);
  digitalWrite(WhiteLight,OFF);
  digitalWrite(GreenLight,OFF);
  delay(300);
  digitalWrite(RedLight,ON);
  digitalWrite(WhiteLight,ON);
  digitalWrite(GreenLight,ON);
  delay(300);
  digitalWrite(RedLight,OFF);
  digitalWrite(WhiteLight,OFF);
  digitalWrite(GreenLight,OFF);
  
}
