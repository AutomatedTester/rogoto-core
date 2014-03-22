from BrickPi import *


speed = 150

BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1


def pen_down():
    BrickPi.MotorSpeed[PORT_A] = speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def pen_up():
    BrickPi.MotorSpeed[PORT_A] = -speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_A] = 0


def forward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * speed
    BrickPi.MotorSpeed[PORT_C] = steps * speed
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[PORT_B] = 0
    BrickPi.MotorSpeed[PORT_C] = 0


def backward(steps):
    BrickPi.MotorSpeed[PORT_B] = steps * -speed
    BrickPi.MotorSpeed[PORT_C] = steps * -speed
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
