#include <BehindTheWire.h>

int power = 0;

void setup() { 

  pinMode(EngineLeft,OUTPUT);
  pinMode(EngineRight,OUTPUT);
  pinMode(RedLight,OUTPUT);

}

void loop() {

  power = map(analogRead(Throttle),0,1024,0,150);
  analogWrite(EngineLeft, power);
  analogWrite(EngineRight, power);

  if (power > 120) {
    digitalWrite(RedLight,ON);
  }
  else {
    digitalWrite(RedLight,OFF);
  }
  delay(100);

}
