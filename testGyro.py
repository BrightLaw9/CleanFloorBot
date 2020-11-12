from BrickPi import * 

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS

BrickPiSetupSensors() 

while True: 
  BrickPiUpdateValues() 
  gyro = BrickPi.Sensor[PORT_1]
  print(str(gyro)) 

