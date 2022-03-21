# Functions: getLeftEncoder(), getRightEncoder()

from BrickPi import * 

class Movement: 
  
  def __init__( self ): 
    pass 
  
  def getLeftEncoder( self ): 
    # OR nMotorEncoder[]
    return BrickPi.Encoder[leftMotor]
