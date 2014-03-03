#include "behindthewire.h"

Servo landingGearServo;
byte lgPos = UP;

void behindthewire::landingGearPrepare() {		// Initiate the servo and set the landing gear to defaults
  landingGearServo.attach(SERVO_PIN, landingGearDownPosition, landingGearUpPosition);
  digitalWrite(UpLight, ON);
  digitalWrite(NotReadyLight, OFF);
  digitalWrite(DownLight, OFF);
  landingGearUp();
}

void behindthewire::landingGearUp() {
  if(lgPos == DOWN){
     for(byte i = 0; i < 180; i++) {
       landingGearServo.write(i);
       delay(landingGearTransitionSpeed);
     }
  }
  lgPos = UP;
}

void behindthewire::landingGearDown() {
  if(lgPos == UP){
     for(byte i = 180; i > 0; i--) {
	    landingGearServo.write(i);
	    delay(landingGearTransitionSpeed);
	 }
  }
  lgPos = DOWN;
}