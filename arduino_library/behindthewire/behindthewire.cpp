#include "BehindTheWire.h"

// Constructor
BehindTheWire::BehindTheWire() {
   lgPos = UP;
   // The servo instance is only allocated on landingGearPrepare()
}


// Destructor 
BehindTheWire::~BehindTheWire() {
  // avr-g++ implementation of delete uses free, which already checks for null
  delete landingGearServo;
}


// Initiate the servo and set the landing gear to defaults
void BehindTheWire::landingGearPrepare() {
   landingGearServo = new Servo();
   landingGearServo->attach(ServoPin, landingGearDownPosition, landingGearUpPosition);

   digitalWrite(UpLight, ON);
   digitalWrite(NotReadyLight, OFF);
   digitalWrite(DownLight, OFF);

   landingGearUp();
}


// Description should go here
void BehindTheWire::landingGearUp() {
   if(lgPos == DOWN) {
      for(byte i=0; i<180; i++) {
         landingGearServo->write(i);
         delay(landingGearTransitionSpeed);
      }
   }
   lgPos = UP;
}


// Description should go here
void BehindTheWire::landingGearDown() {
   if(lgPos == UP) {
      for(byte i=180; i>0; i--) {
         landingGearServo->write(i);
         delay(landingGearTransitionSpeed);
      }
   }
   lgPos = DOWN;
}