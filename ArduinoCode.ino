
#include <Servo.h>

Servo panServo;

int pos = 90;

void setup()
{
  Serial.begin(115200);
  panServo.attach(9);
}

void loop()
{

  if(Serial.available())
  {
    int a = Serial.parseInt();
    if(a==1)    
    {
      pos -=10;
      pos = constrain(pos,10,170);
           panServo.write(pos);
    }
    if(a == 2)
    {
    pos += 10;
     pos= constrain(pos,10,170);
         panServo.write(pos);
    }
    if(a==3)    
    {
      pos -=10;
      
      pos =constrain(pos,10,170);
           panServo.write(pos);
    }
    if(a == 4)
    {
  
      pos += 10;
      
      pos =constrain(pos,10,170);
      panServo.write(pos);
  
  
  }
  
  }
      Serial.println(pos);


  delay(1);
  
}
  
