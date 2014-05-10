#include <BehindTheWire.h>
#include <Servo.h> 

BehindTheWire functions;

int ButtonLeft = 0;
int ButtonRight = 0;

void setup() {

  pinMode(LeftButton,INPUT);         // Make the Up Button an Input
  pinMode(RightButton,INPUT);        // Make the Down Button an Input
  functions.rudderPrepare();         // Set up the landing gear

}

void loop() {

  ButtonLeft = digitalRead(LeftButton);     // Get the state of Up Button
  ButtonRight = digitalRead(RightButton);   // Get the state of Down Button

  if(ButtonLeft == PRESSED) {
    functions.rudderLeft();
  }
    
  if(ButtonRight == PRESSED) {
    functions.rudderRight();
  }

}