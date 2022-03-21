from BrickPi import * 

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS

BrickPiSetupSensors() 

class Gyro: 
  
  def __init__( self ): 
    self.angle = BrickPi.Sensor[PORT_1] 
  
  def getHeading( self ): 
    return self.angle 

