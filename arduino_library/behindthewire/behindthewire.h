// -*- Mode: C++; c-basic-offset: 8; indent-tabs-mode: nil -*-
#ifndef behindthewire_h
#define behindthewire_h

#if defined(ARDUINO) && ARDUINO >= 100
   #include "Arduino.h"
#else
   #include "WProgram.h"
#endif
#include "../Servo/Servo.h"

// States
#define PRESSED           HIGH
#define NOT_PRESSED       LOW
#define ON                HIGH
#define OFF               LOW
#define UP                HIGH
#define DOWN              LOW

// IO pins
#define LedRedPin         13
#define LedYellowPin      12
#define LedGreenPin       11
#define ButtonTopPin      9
#define ButtonBottomPin   8
#define PotPin            A0
#define ServoPin          6
#define MotorPin          3

// LED and Button pins
#define RedLight          LedRedPin
#define YellowLight       LedYellowPin
#define GreenLight        LedGreenPin
#define OnButton          ButtonTopPin
#define OffButton         ButtonBottomPin

// Landing Gear
#define UpLight           LedRedPin
#define DownLight         LedGreenPin
#define NotReadyLight     LedYellowPin
#define UpButton          ButtonTopPin
#define DownButton        ButtonBottomPin

// Engine Speed
#define Engine            MotorPin
#define Throttle          PotPin

// Tunable constants for landing gear
#define landingGearDownPosition      1600
#define landingGearUpPosition        2400
#define landingGearTransitionSpeed   20


class BehindTheWire {
public:
   BehindTheWire();
   //~BehindTheWire();
   //void begin();
   void landingGearPrepare();
   void landingGearUp();
   void landingGearDown();
   
private:
   static Servo landingGearServo;
   byte lgPos;
};

#endif // behindthewire_h