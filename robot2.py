from gpiozero import Robot
import time


robot = Robot(left=(27,17,25), right=(24,23,22))

def delay(secs=0.1):
    time.sleep(secs)

while True:
    a = str(input())
    if a == 'w':
        robot.forward()
        delay()
    elif a == 's':
        robot.backward()
        delay()
    elif a == 'a':
        robot.left()
        delay()
    elif a == 'd':
        robot.right()
        delay()
    else:
        print(n)
    robot.stop()
        