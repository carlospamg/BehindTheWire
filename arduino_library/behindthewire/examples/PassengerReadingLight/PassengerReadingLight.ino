#include <BehindTheWire.h>

int ButtonOn = 0;
int ButtonOff = 0;

void setup() {

  pinMode(RedLight,OUTPUT);             //Make the Red Light an Output
  pinMode(OnButton,INPUT);              //Make the On Button an Input
  pinMode(OffButton,INPUT);             //Make the OffButton an Input

}

void loop() {

  ButtonOn = digitalRead(OnButton);     //Get the state of On Button
  ButtonOff = digitalRead(OffButton);   //Get the state of Off Button

  if(ButtonOn == PRESSED) {             // Has On button been pressed?
    digitalWrite(RedLight,ON);          // Turn the red light on
  }
  
  if(ButtonOff == PRESSED) {            // Has Off button been pressed?
    digitalWrite(RedLight,OFF);         // Turn the red light off
  }
  
  delay(100);

}
