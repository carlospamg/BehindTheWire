#include <BehindTheWire.h>
#include <Servo.h>

int ButtonLeft = 0;
int ButtonRight = 0;
int power = 0;
int angle = 0;
int old_power = 0;
BehindTheWire functions;

void setup() {

  pinMode(RedLight,OUTPUT);             // Make the red Light an Output
  pinMode(WhiteLight,OUTPUT);           // Make the white Light an Output
  pinMode(GreenLight,OUTPUT);           // Make the green Light an Output
  pinMode(LeftButton,INPUT);            // Make the On/Left Button an Input
  pinMode(RightButton,INPUT);           // Make the Off/Right Button an Input
  pinMode(EngineLeft,OUTPUT);           // Make the Left Engine an Output
  pinMode(EngineRight,OUTPUT);          // Make the Left Engine an Output

  functions.rudderPrepare();            // Set up the rudder

  // Blink lights to prove they are working without further input
  digitalWrite(RedLight,ON);
  delay(300);
  digitalWrite(WhiteLight,ON);
  delay(300);
  digitalWrite(GreenLight,ON);
  delay(300);
  digitalWrite(RedLight,OFF);
  digitalWrite(WhiteLight,OFF);
  digitalWrite(GreenLight,OFF);
  delay(300);
  digitalWrite(RedLight,ON);
  digitalWrite(WhiteLight,ON);
  digitalWrite(GreenLight,ON);

  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  } 
  Serial.println("Sucessful start:"); 

}

void loop() {

  // Read pot
  power = map(analogRead(Throttle),0,1024,0,255);
  angle = map(power,0,255,-45,45);
  if(power != old_power) {
    Serial.println(power);  
    old_power = power;
  }  

  // Set motors and move servo based on pot
  analogWrite(EngineLeft, power);
  analogWrite(EngineRight, power); 
  functions.rudderSetPosition(angle);

  // Check buttons and LEDs
  ButtonLeft = digitalRead(LeftButton);   // Get the state of On/Left Button
  if(ButtonLeft == PRESSED) {             // Has On button been pressed?
    Serial.println("Left");
    digitalWrite(RedLight,ON);            // Turn the red light on
    digitalWrite(WhiteLight,ON);          // Turn the white light on
    digitalWrite(GreenLight,ON);          // Turn the green light on
    functions.rudderLeft();
  }

  ButtonRight = digitalRead(RightButton);   // Get the state of Off/Right Button
  if(ButtonRight == PRESSED) {              // Has Off button been pressed?
    Serial.println("Right");
    digitalWrite(RedLight,OFF);
    digitalWrite(WhiteLight,OFF);
    digitalWrite(GreenLight,OFF);
    functions.rudderRight();
  }

  delay(100);

}
