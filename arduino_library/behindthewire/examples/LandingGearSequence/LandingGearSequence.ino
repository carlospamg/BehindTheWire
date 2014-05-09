#include <BehindTheWire.h>
#include <Servo.h> 

BehindTheWire functions;

int ButtonUp = 0;
int ButtonDown = 0;

void setup() {

  pinMode(UpButton,INPUT);                // Make the Up Button an Input
  pinMode(DownButton,INPUT);              // Make the Down Button an Input
  functions.landingGearPrepare();         // Set up the landing gear

}

void loop() {

  ButtonUp = digitalRead(UpButton);       // Get the state of Up Button
  ButtonDown = digitalRead(DownButton);   // Get the state of Down Button

  if(ButtonUp == PRESSED) {
    functions.landingGearUp();
  }
    
  if(ButtonDown == PRESSED) {
    functions.landingGearDown();
  }

}