// -*- Mode: C++; c-basic-offset: 8; indent-tabs-mode: nil -*-
#ifndef _BehindTheWire_h
#define _BehindTheWire_h

#if defined(ARDUINO) && ARDUINO >= 100
   #include "Arduino.h"
#else
   #include "WProgram.h"
#endif

//#include <Servo.h>
#if defined(ARDUINO) && ARDUINO >= 150
   #include "../Servo/src/Servo.h"
#else
   #include "../Servo/Servo.h"
#endif


// States
#define PRESSED           HIGH
#define NOT_PRESSED       LOW
#define ON                HIGH
#define OFF               LOW
#define UP                HIGH
#define DOWN              LOW

// IO pins
#define LedRedPin         A0
#define LedWhitePin       A1
#define LedGreenPin       10
#define ButtonLeftPin     A2
#define ButtonRightPin    A3
#define PotPin            A5
#define ServoPin          11
#define MotorLeftPin      3
#define MotorRightPin     5

// The following are the old pinouys
// present only temporarily for debugging
//#define LedRedPin         13
//#define LedWhitePin       12
//#define LedYellowPin      12
//#define LedGreenPin       11
//#define ButtonLeftPin     9
//#define ButtonRightPin    8
//#define PotPin            A0
//#define ServoPin          6
//#define MotorPin          3
//#define MotorLeftPin      3
//#define MotorRightPin     3
// End of old pins

// General component names
#define RedLight          LedRedPin
#define YellowLight       LedWhitePin
#define WhiteLight        LedWhitePin
#define GreenLight        LedGreenPin

#define OnButton          ButtonLeftPin
#define OffButton         ButtonRightPin
#define LeftButton        ButtonLeftPin
#define RightButton       ButtonRightPin

#define EngineLeft        MotorLeftPin
#define EngineRight       MotorRightPin

// Landing Gear specific names
#define UpLight           LedRedPin
#define DownLight         LedGreenPin
#define NotReadyLight     LedWhitePin
#define UpButton          ButtonLeftPin
#define DownButton        ButtonRightPin

// Engine Speed
#define Throttle          PotPin

// Tunable constants for landing gear
#define landingGearDownPosition      1600
#define landingGearUpPosition        2400
#define landingGearTransitionSpeed   20


class BehindTheWire {
public:
   BehindTheWire();
   ~BehindTheWire();
   //void begin();
   //void end();
   void landingGearPrepare();
   void landingGearUp();
   void landingGearDown();
   
private:
   byte lgPos;

   // Pointers with dynamic memory allocation is not ideal 
   // in this kind of system, but it resolves having to
   // import the Servo library when rudder is not in use.
   Servo *landingGearServo;
};

#endif // _BehindTheWire_h
