from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = EV3_GYRO_ABS_DPS
BrickPi.SensorType[PORT_2] = NXT_ULTRASONIC
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_D] = 1

BrickPiSetupSensors()
