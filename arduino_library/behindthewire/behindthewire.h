// -*- Mode: C++; c-basic-offset: 8; indent-tabs-mode: nil -*-

#include <Servo.h>

#if defined(ARDUINO) && ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif

#ifndef behindthewire_h
#define behindthewire_h

//Defines
#define PRESSED HIGH
#define NOT_PRESSED LOW
#define ON HIGH
#define OFF LOW

#define RedLight 13
#define YellowLight 12
#define GreenLight 11
#define OnButton 9
#define OffButton 8

// Landing gear
#define UpLight 13
#define DownLight 11
#define UpButton 9
#define DownButton 8
#define NotReadyLight 12
#define SERVO_PIN 6

#define UP 1
#define DOWN 0

#define Engine 3
#define Throttle A0

// Tunable constants for landing gear
#define landingGearDownPosition 1600
#define landingGearUpPosition 2400
#define landingGearTransitionSpeed 20

class behindthewire {

	public:
		void landingGearPrepare();
		void landingGearUp();
		void landingGearDown();
};

#endif // behindthewire_h