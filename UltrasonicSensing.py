from BrickPi import * 

BrickPiSetup() 
BrickPi.SensorType[PORT_2] = NXT_ULTRASONIC 


class UltrasonicSensing: 

  def __init__( self ): 
      pass 
  
  def getDistance( self ): 
      distance = BrickPi.Sensor[PORT_2]
      return distance 
      
