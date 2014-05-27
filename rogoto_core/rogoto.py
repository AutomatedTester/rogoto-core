from BrickPi import *


speed = 150

BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1


def pen_down():
    '''
        Tell motor on PORT_A to move. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_A] = speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def pen_up():
    '''
        Tell motor on PORT_A to move. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_A] = -speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def forward(steps):
    '''
        Tell motor on PORT_B and PORT_C to move. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_B] = steps * speed
    BrickPi.MotorSpeed[PORT_C] = steps * speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def backward(steps):
    '''
        Tell motor on PORT_B and PORT_C to move. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_B] = steps * -speed
    BrickPi.MotorSpeed[PORT_C] = steps * -speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def left(deg):
    '''
        Tell motor on PORT_B and PORT_C to move in opposite directions. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_B] = deg * speed
    BrickPi.MotorSpeed[PORT_C] = deg * -speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def right(deg):
    '''
        Tell motor on PORT_B and PORT_C to move in opposite directions. When complete the motor speed is reset
    '''
    BrickPi.MotorSpeed[PORT_C] = deg * speed
    BrickPi.MotorSpeed[PORT_B] = deg * -speed
    BrickPiUpdateValues()

    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0
