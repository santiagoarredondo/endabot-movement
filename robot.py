# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3 = 17
in4 = 27

en = 25
en2 = 22
temp1=1
GPIO.setmode(GPIO.BCM)
#Motor 1
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.HIGH)
p=GPIO.PWM(en,1000)
#Motor 2
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.HIGH)
p=GPIO.PWM(en2,1000)

 

def go_forward():
    return 0

def go_back():
    return 0

def go_left():
    return 0

def go_right():
    return 0

if __name__ == '__main__':
    
    p.start(25)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")   
    
    while(1):

        x=input()
        
        if x=='r':
            print("run")
            if(temp1==1):
             GPIO.output(in1,GPIO.HIGH)
             GPIO.output(in2,GPIO.LOW)
             GPIO.output(in3,GPIO.HIGH)
             GPIO.output(in4,GPIO.LOW)
             print("forward")
             x='z'
            else:
             GPIO.output(in1,GPIO.LOW)
             GPIO.output(in2,GPIO.HIGH)
             GPIO.output(in3,GPIO.LOW)
             GPIO.output(in4,GPIO.HIGH)
             print("backward")
             x='z'


        elif x=='s':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            temp1=1
            x='z'

        elif x=='b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            temp1=0
            x='z'

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            p.ChangeDutyCycle(75)
            x='z'
         
        
        elif x=='e':
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
