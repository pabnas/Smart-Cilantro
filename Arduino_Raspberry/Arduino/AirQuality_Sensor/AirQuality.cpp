/*
  AirQuality library v1.0
  2010 Copyright (c) Seeed Technology Inc.  All right reserved.
 
  Original Author: Bruce.Qin
  
  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/
#include"Arduino.h"
#include"AirQuality.h"

//Get the avg voltage in 5 minutes.

void AirQuality::avgVoltage()
{
	if(i==150)//sum 5 minutes
	{
		vol_standard=temp/150; 
		temp=0;
		Serial.print("Vol_standard in 5 minutes:");			
		Serial.println(vol_standard);		
		i=0;		
	}
    else 
	{
		temp+=first_vol;
		i++;
	}
}
void AirQuality::init(int pin)
{
    _pin=pin;
    pinMode(_pin,INPUT);
    unsigned char i=0;
    delay(3000);
    Serial.println("sys_starting...");
    //delay(20000);//200000
    init_voltage=analogRead(_pin);

    //Serial.println("The init voltage is ...");
    //Serial.println(init_voltage);
    while(init_voltage)
    {
        if(init_voltage<798 && init_voltage>10)// the init voltage is ok
        {
            first_vol=analogRead(A0);//initialize first value
            last_vol=first_vol;
            vol_standard=last_vol;
            //Serial.println("Sensor ready.");
            error=false;;
            break;
        }
        else if(init_voltage>798||init_voltage<=10)
        {	
            i++;
            Serial.println("waitting sensor init..(it takes 60 seconds to init)");
            delay(60000);//60000
            init_voltage=analogRead(A0);
            if(i==5)
            {
                i=0;
                error=true;
                Serial.println("Sensor Error!");
            }
          }
        else 
        break;
    }
    //init the timer 
    TCCR1A=0;//normal model
    TCCR1B=0x02;//set clock as 8*(1/16M)
    TIMSK1=0x01;//enable overflow interrupt
    Serial.println("Test begin...");
    sei();
}
int AirQuality::slope(bool mostrar)
{
  while(timer_index)
	{
    	if(first_vol-last_vol>400||first_vol>700)
        {
            if(mostrar == true)
                Serial.println("High pollution! Force signal active.");		
            timer_index=0;	
            //avgVoltage();	
            return first_vol;	
        }
    	else if((first_vol-last_vol>400&&first_vol<700)||first_vol-vol_standard>150)
        {	
            if(mostrar == true)
            {
                Serial.print("sensor_value:");		
                Serial.print(first_vol);      		
                Serial.println("\t High pollution!");		
            }
            timer_index=0;	
            //avgVoltage();
            return first_vol;
            
        }
    	else if((first_vol-last_vol>200&&first_vol<700)||first_vol-vol_standard>50)
        {
            //Serial.println(first_vol-last_vol);
            if(mostrar == true)
            {
                Serial.print("sensor_value:");
                Serial.print(first_vol);      		
                Serial.println("\t Low pollution!");		
            }
            timer_index=0;
            //avgVoltage();
            return first_vol;	
        }
    	else
        {
            //avgVoltage();	
            if(mostrar == true)
            {
                Serial.print("sensor_value:");
                Serial.print(first_vol);
                Serial.println("\t Air fresh");
            }
            timer_index=0;
            return first_vol;
        }
	}
    return -1;
}

