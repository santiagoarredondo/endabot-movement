/*
 * sin título.c
 * 
 * Copyright 2019  <pi@raspberrypi>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

#define IN1  27   //K1、K2 motor direction
#define IN2  28    //K1、K2 motor direction
#define IN3  23    //K3、K4 motor direction
#define IN4  24  //K3、K4 motor direction

#define ENA  1    // Needs to be a PWM pin to be able to control motor speed ENA
#define ENB  26   // Needs to be a PWM pin to be able to control motor speed ENA

void set_motorspeed(int lspeed,int rspeed) //change motor speed
{
  softPwmWrite(ENA,lspeed);//lspeed:0-255
  softPwmWrite(ENB,rspeed);//rspeed:0-255   
}

void setup() {
  
 /******L298N******/
  pinMode(IN1, OUTPUT); 
  pinMode(IN2, OUTPUT); 
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT); 
  pinMode(ENA, OUTPUT);  
  pinMode(ENB, OUTPUT);
  set_motorspeed(220,220);
}

void go_ahead() //motor rotate counterclockwise -->robot go back
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4,LOW); 
}

int main(int argc, const char* arg[])
{
	setup();
	wiringPiSetup();
	for(;;){
		go_ahead();
		printf("hola");
	}
}
