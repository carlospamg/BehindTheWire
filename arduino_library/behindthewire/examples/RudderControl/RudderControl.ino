#include <BehindTheWire.h>
#include <Servo.h> 

BehindTheWire functions;

int ButtonLeft = 0;
int ButtonRight = 0;

void setup() {

  pinMode(LeftButton,INPUT);         // Make the Left Button an Input
  pinMode(RightButton,INPUT);        // Make the Right Button an Input
  functions.rudderPrepare();         // Set up the rudder in position

}

void loop() {

  ButtonLeft = digitalRead(LeftButton);     // Get the state of Left Button
  ButtonRight = digitalRead(RightButton);   // Get the state of Right Button

  if(ButtonLeft == PRESSED) {
    functions.rudderLeft();
  }
    
  if(ButtonRight == PRESSED) {
    functions.rudderRight();
  }

}