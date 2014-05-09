#include <BehindTheWire.h>
#include <Servo.h>

int ButtonLeft = 0;
int ButtonRight = 0;
int power = 0;
BehindTheWire functions;

void setup() {

  pinMode(RedLight,OUTPUT);             // Make the red Light an Output
  pinMode(WhiteLight,OUTPUT);           // Make the white Light an Output
  pinMode(GreenLight,OUTPUT);           // Make the green Light an Output
  pinMode(LeftButton,INPUT);            // Make the On Button an Input
  pinMode(RightButton,INPUT);           // Make the Off Button an Input
  pinMode(EngineLeft,OUTPUT);           // Make the Left Engine an Output
  pinMode(EngineRight,OUTPUT);          // Make the Left Engine an Output
  functions.landingGearPrepare();       // Set up the landing gear

}

void loop() {

  ButtonLeft = digitalRead(LeftButton);     // Get the state of On Button
  ButtonRight = digitalRead(RightButton);   // Get the state of Off Button
  
  power = map(analogRead(Throttle),0,1024,0,255);
  analogWrite(EngineLeft, power);
  analogWrite(EngineRight, power); 

  if(ButtonLeft == PRESSED) {             // Has On button been pressed?
    digitalWrite(RedLight,ON);          // Turn the red light on
    digitalWrite(WhiteLight,ON);        // Turn the white light on
    digitalWrite(GreenLight,ON);        // Turn the green light on
    functions.landingGearUp();
  }
  
  if(ButtonRight == PRESSED) {            // Has Off button been pressed?
    digitalWrite(RedLight,OFF);         // Turn the red light off
    digitalWrite(WhiteLight,OFF);       // Turn the white light off
    digitalWrite(GreenLight,OFF);       // Turn the green light off
    functions.landingGearDown();
  }
  
  delay(100);
  
}
