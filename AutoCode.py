from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS
BrickPi.SensorType[PORT_2] = NXT_ULTRASONIC
BrickPi.MotorEnable[PORT_A] = 1 #Left
BrickPi.MotorEnable[PORT_D] = 1 #Right

BrickPiSetupSensors() 

def move(speedLeft, speedRight): 
  BrickPi.MotorSpeed[PORT_A] = speedLeft
  BrickPi.MotorSpeed[PORT_D] = speedRight 

def new_lane(): 
  while abs_angle < 90: 
        move(-75, 75)

while True: 
  BrickPiUpdateValues() 
  distance = BrickPi.Sensor[PORT_2] 
  abs_angle = BrickPi.Sensor[PORT_1] 
 
  
  #Check if approaching a wall 
  #Is the measurement done in cm?  
  if distance < 1000:  
     new_lane()
  #Realigning the robot to continue in a straight line
    elif abs_angle >= 1: 
      move(-75, 75)
    elif abs_angle <= 1: 
      move(75, -75)
        
     
    
  
  
  
