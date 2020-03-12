/*
  AirQuality Demo V1.0.
  connect to A0 to start testing. it will needs about 20s to start 
* By: http://www.seeedstudio.com
*/

#include"AirQuality.h"
#include"Arduino.h"
AirQuality airqualitysensor;
int current_quality =-1;

int sensorpin_humedad = A1;


void setup()
{
   Serial.begin(9600);
   airqualitysensor.init(14);
}

void loop()
{
  int humedad = analogRead(sensorpin_humedad);
  humedad = 1023-humedad;
  
  current_quality=airqualitysensor.slope(false);
  if (current_quality >= 0)
  {
      Serial.print(humedad);
      Serial.print(" , ");
      Serial.println(current_quality);
  }
  delay(1000);
}


ISR(TIMER1_OVF_vect)
{
  if(airqualitysensor.counter==61)//set 2 seconds as a detected duty
  {
    airqualitysensor.last_vol=airqualitysensor.first_vol;
    airqualitysensor.first_vol=analogRead(A0);
    airqualitysensor.counter=0;
    airqualitysensor.timer_index=1;
    PORTB=PORTB^0x20;
  }
  else
  {
    airqualitysensor.counter++;
  }
}
