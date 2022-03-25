from re import X
import tkinter as tk

class Bud:
    def __init__(self, xSpeed, ySpeed, colony):
        self.foodLevel = 0
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.colony = colony

    