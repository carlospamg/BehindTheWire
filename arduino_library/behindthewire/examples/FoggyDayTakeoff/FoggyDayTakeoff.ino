#include <BehindTheWire.h>      //The magic behind the wire

void setup() {

  pinMode(RedLight,OUTPUT);     //Make the Red Light an Output

}

void loop() {

  digitalWrite(RedLight,ON);    // Turn the red light on
  delay(1000);                  // Wait for 1 second (1000ms)
  digitalWrite(RedLight,OFF);   // Turn the red light off
  delay(1000);                  // Wait for 1 second (1000ms)

}
