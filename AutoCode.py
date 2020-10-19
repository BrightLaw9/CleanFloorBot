from BrickPi import *
from time import sleep

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS
BrickPi.SensorType[PORT_2] = NXT_ULTRASONIC
BrickPi.MotorEnable[PORT_A] = 1 #Left
BrickPi.MotorEnable[PORT_D] = 1 #Right

BrickPiSetupSensors() 

def move(speedLeft, speedRight): 
  BrickPi.MotorSpeed[PORT_A] = speedLeft
  BrickPi.MotorSpeed[PORT_D] = speedRight 

count = 0
def new_lane_right(): 
  while abs_angle < 90: 
    move(-75, 75)
  move(75, 75)
  time.sleep(3)
  while abs_angle < 180: 
    move(-75, 75) 
  count += 1
  
def new_lane_left(): 
  while abs_angle > 90: 
    move(75, -75)
  move(75, 75)
  time.sleep(3)
  while abs_angle > 0: 
    move(75, -75) 
  count += 1
  
while True: 
  BrickPiUpdateValues() 
  distance = BrickPi.Sensor[PORT_2] 
  abs_angle = BrickPi.Sensor[PORT_1] 
 
  
  #Check if approaching a wall 
  #Is the measurement done in cm?  
  if distance < 20 and (count % 2) == 1:
    new_lane_right
    elif distance < 20 and (count % 2) == 0:   
      new_lane_left
  #Realigning the robot to continue in a straight line
    elif abs_angle >= 1: 
      move(-75, 75)
    elif abs_angle <= 1: 
      move(75, -75)
        
     
    
  
  
  
