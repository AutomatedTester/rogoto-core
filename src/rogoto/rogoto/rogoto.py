from BrickPi import *


BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1


def pen_down():
    BrickPi.MotorSpeed[PORT_A] = 100
    BrickPiUpdateValues()


def pen_up():
    BrickPi.MotorSpeed[PORT_A] = -100
    BrickPiUpdateValues()


def forward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * 10
    BrickPi.MotorSpeed[PORT_C] = steps * 10
    BrickPiUpdateValues()


def backward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * -10
    BrickPi.MotorSpeed[PORT_C] = steps * -10
    BrickPiUpdateValues()


def left(deg):
    BrickPi.MotorSpeed[PORT_B] = deg
    BrickPiUpdateValues()


def right(deg):
    BrickPi.MotorSpeed[PORT_C] = deg
    BrickPiUpdateValues()
