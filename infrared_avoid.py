#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 9:59 下午
# @Author  : Dynasty
# @File    : infrared_avoid.py
# @Software: PyCharm
import RPi.GPIO as GPIO
from basic_control import BasicControl


class InfraredAvoid(BasicControl):
    def __init__(self):
        BasicControl.__init__(self)
        self.SensorRight = 16
        self.SensorLeft = 12

        BtnPin = 19
        Gpin = 5
        Rpin = 6
        GPIO.setup(Gpin, GPIO.OUT)  # Set Green Led Pin mode to output
        GPIO.setup(Rpin, GPIO.OUT)  # Set Red Led Pin mode to output
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.setup(self.SensorRight, GPIO.IN)
        GPIO.setup(self.SensorLeft, GPIO.IN)

    def avoid_obstacle(self, speed):
        SL_2 = GPIO.input(self.SensorLeft)
        SR_2 = GPIO.input(self.SensorRight)
        # 左边有障碍
        if SL_2 == 0 and SR_2 == 1:
            print("turn right")
            self.t_right(30, 0.3)
            self.t_up(speed)
        # 右边有障碍
        elif SL_2 == 1 and SR_2 == 0:
            print("turn left")
            self.t_left(30, 0.3)
            self.t_up(speed)
        # 前方有障碍
        elif SL_2 == 0 and SR_2 == 0:
            self.t_stop(0.3)
            self.t_down(30, 0.4)
            self.t_left(30, 0.5)
            self.t_up(speed)
