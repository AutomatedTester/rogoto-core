from BrickPi import *


BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1


def pen_down():
    BrickPi.MotorSpeed[PORT_A] = 100
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def pen_up():
    BrickPi.MotorSpeed[PORT_A] = -100
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def forward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * 10
    BrickPi.MotorSpeed[PORT_C] = steps * 10
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def backward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * -10
    BrickPi.MotorSpeed[PORT_C] = steps * -10
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def left(deg):
    BrickPi.MotorSpeed[PORT_B] = deg
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0


def right(deg):
    BrickPi.MotorSpeed[PORT_C] = deg
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_C] = 0
