import BrickPiJava

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS

BrickPiSetupSensors() 

public class Gyro: 
  
  public Gyro():  
    this.angle = BrickPi.Sensor[PORT_1] 
  
  public double getHeading(): 
    return self.angle 

