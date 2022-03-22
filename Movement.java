// Functions: getLeftEncoder(), getRightEncoder()

from BrickPi import * 

public class Movement { 
  public Movement() {  
    pass 
    }
  
  public void getLeftEncoder() { 
    # OR nMotorEncoder[]
    return BrickPi.Encoder[leftMotor]
    }

  } 
