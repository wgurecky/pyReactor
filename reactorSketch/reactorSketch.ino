#include <Servo.h>

Servo myServo;
int servoPin = 9;
int ledRGBRedPin = 12;
int ledRGBGreenPin = 10;
int ledRGBBluePin = 11;
int ledRedPin = 13;

void setup(void){
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo.write(5);  //set default position
  pinMode(ledRGBRedPin, OUTPUT);
  pinMode(ledRGBBluePin, OUTPUT);
  pinMode(ledRGBGreenPin, OUTPUT);
  pinMode(ledRedPin, OUTPUT);
  analogWrite(ledRGBRedPin, 0);
  analogWrite(ledRGBGreenPin, 0);
  analogWrite(ledRGBBluePin, 0);
  analogWrite(ledRedPin, 0);
  loop();
}

void loop(void){
  int ledPowerSetting;
  int rodHeightSetting;
  int scramCondition;
  if (Serial.available() > 0)
  {
    char inByte = Serial.read();
    switch(inByte)
    {
    case 'p': //power
      // led glows blue
      ledPowerSetting = numberFromSerial();
      analogWrite(ledRGBRedPin, 0);
      analogWrite(ledRGBGreenPin, 0);
      analogWrite(ledRGBBluePin, ledPowerSetting);
      break;
    case 'r': //rod position
      rodHeightSetting = numberFromSerial();
      myServo.write(rodHeightSetting);
      break;
    case 's': //scram condition
      // led glows red
      scramCondition = numberFromSerial();
      // 0 (0v) to 1023 (5v)
      analogWrite(ledRGBGreenPin, 0);
      analogWrite(ledRGBBluePin, 0);
      analogWrite(ledRGBRedPin, scramCondition);
      break;
    }
    Serial.flush();
  }
}
 
int numberFromSerial(void)
{
  char numberString[8];
  unsigned char index=0;
  delay(10);
  while(Serial.available() > 0)
  {
    delay(10);
    numberString[index++]=Serial.read();
    if(index>6)
    {
      break;
    }
  }
  numberString[index]=0;
  return atoi(numberString);
}
