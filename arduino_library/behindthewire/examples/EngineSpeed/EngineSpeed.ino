#include <Servo.h>
#include <behindthewire.h>

int power = 0;

void setup()
{ 
  pinMode(Engine,OUTPUT);
}

void loop()
{
   power = map(analogRead(Throttle),0,1024,0,255);
   analogWrite(Engine, power); 
   if (power > 200)
   {
      digitalWrite(RedLight,ON);
   }
   else
   {
      digitalWrite(RedLight,OFF);
   }
}

