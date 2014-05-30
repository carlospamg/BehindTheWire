#include "BehindTheWire.h"


/** Constructor */
BehindTheWire::BehindTheWire() {
   lgPos = UP;
   // The servo instance is only allocated on landingGearPrepare()
}


/** Destructor */
BehindTheWire::~BehindTheWire() {
  // avr-g++ implementation of delete uses free, which already checks for null
  delete servoInstance;
}


/** Instantiates the servo pointer and configures it */
void BehindTheWire::servoPrepare() {
   servoInstance = new Servo();
   servoInstance->attach(ServoPin, servoRightPosition, servoLeftPosition);
}


// /////////////////////////////
//  Rudder Specific functions //
// /////////////////////////////

/** Initiates the servo and sets the rudder to the centre position */
void BehindTheWire::rudderPrepare() {
   servoPrepare();
   rudderCentre();
}


/** Move the rudder to the LEFT position */
void BehindTheWire::rudderLeft() {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }

   byte currentPosition = servoInstance->read();
   if(currentPosition < 180) {
      for(byte i=currentPosition; i<180; i++) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }
   }
}


/** Move the rudder to the CENTRE position */
void BehindTheWire::rudderCentre() {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }
   rudderSetPosition(0);
}


/** Move the rudder to the RIGHT position */
void BehindTheWire::rudderRight() {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }

   byte currentPosition = servoInstance->read();
   if(currentPosition > 0) {
      for(byte i=currentPosition; i>0; i--) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }
   }
}


/** Sets the servo position to the input argument
 *  The input is based on a -45 to 45 degrees format and uses the
 *  int argument as it's the only type we general introduce in workshops
 */
void BehindTheWire::rudderSetPosition(int newPosition) {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }

   // Conver -45,45 range to 0,180 range and clipping out of range values
   newPosition <<= 1;
   newPosition += 90;
   newPosition = (newPosition>180) ? 180 : newPosition;
   newPosition = (newPosition<0) ? 0 : newPosition;

   byte currentPosition = servoInstance->read();
   if(newPosition > currentPosition) {
      for(byte i=currentPosition; i<newPosition; i++) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }   
   } else if(newPosition < currentPosition) {
      for(byte i=currentPosition; i>newPosition; i--) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }
   }
   // Else, the current position and requested are the same
}


// ////////////////////////////////////
//   Landing Gear Specific functions //
// ////////////////////////////////////

/** Initiate the servo and set the landing gear to defaults */
void BehindTheWire::landingGearPrepare() {
   servoPrepare();

   digitalWrite(UpLight, ON);
   digitalWrite(NotReadyLight, OFF);
   digitalWrite(DownLight, OFF);

   landingGearUp();
}


/** Move the landing gear to the UP position */
void BehindTheWire::landingGearUp() {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }

   if(lgPos == DOWN) {
      for(byte i=0; i<180; i++) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }
   }
   lgPos = UP;
}


/** Move the landing gear to the DOWN position */
void BehindTheWire::landingGearDown() {
   if(servoInstance == NULL) {
      // Return instead of calling servoPrepare() so that it
      // is clear something is not working w/o crashing
      return;
   }

   if(lgPos == UP) {
      for(byte i=180; i>0; i--) {
         servoInstance->write(i);
         delay(servoTransitionSpeed);
      }
   }
   lgPos = DOWN;
}
