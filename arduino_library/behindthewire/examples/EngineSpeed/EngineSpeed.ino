#include <BehindTheWire.h>

int power = 0;

void setup() { 

  pinMode(EngineLeft,OUTPUT);
  pinMode(EngineRight,OUTPUT);
  
}

void loop() {

   power = map(analogRead(Throttle),0,1024,0,255);
   analogWrite(EngineLeft, power);
   analogWrite(EngineRight, power);

   if (power > 200) {
      digitalWrite(RedLight,ON);
   }
   else {
      digitalWrite(RedLight,OFF);
   }

}
