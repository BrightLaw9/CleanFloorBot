# For odometry calculations to determine where the robot is (pose) 

import pose
import gyro 
import Math 
import movement 

class Odometry: 
  
  def __init__( self ): 
    self.leftDistance = movement.getLeftEncoder()
    self.rightDistance = movement.getRightEncoder() 
    self.angle = gyro.getHeading() 
   
  def calculateNewPose( self ): 
    # delta-x = (lDistance + rDistance) / 2 * cos(theta + delta theta / 2) 
