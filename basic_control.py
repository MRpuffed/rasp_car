#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 8:05 下午
# @Author  : Dynasty
# @File    : basic_control.py
# @Software: PyCharm
import RPi.GPIO as GPIO
import time


class BasicControl(object):
    def __init__(self):
        self.PWMA = PWMA = 18
        self.AIN1 = AIN1 = 22
        self.AIN2 = AIN2 = 27

        self.PWMB = PWMB = 23
        self.BIN1 = BIN1 = 25
        self.BIN2 = BIN2 = 24

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AIN2, GPIO.OUT)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(PWMA, GPIO.OUT)

        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)
        GPIO.setup(PWMB, GPIO.OUT)

        self.L_Motor = GPIO.PWM(PWMA, 100)
        self.L_Motor.start(0)

        self.R_Motor = GPIO.PWM(PWMB, 100)
        self.R_Motor.start(0)

    def t_up(self, speed, t_time=0):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.AIN2, False)  # AIN2
        GPIO.output(self.AIN1, True)   # AIN1

        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.BIN2, False)  # BIN2
        GPIO.output(self.BIN1, True)   # BIN1
        time.sleep(t_time)

    def t_stop(self, t_time=0):
        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.AIN2, False)  # AIN2
        GPIO.output(self.AIN1, False)  # AIN1

        self.R_Motor.ChangeDutyCycle(0)
        GPIO.output(self.BIN2, False)  # BIN2
        GPIO.output(self.BIN1, False)  # BIN1
        time.sleep(t_time)

    def t_down(self, speed, t_time=0):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.AIN2, True)  # AIN2
        GPIO.output(self.AIN1, False)  # AIN1

        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.BIN2, True)  # BIN2
        GPIO.output(self.BIN1, False)  # BIN1
        time.sleep(t_time)

    def t_left(self, speed, t_time=0):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.AIN2, True)  # AIN2
        GPIO.output(self.AIN1, False)  # AIN1

        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.BIN2, False)  # BIN2
        GPIO.output(self.BIN1, True)  # BIN1
        time.sleep(t_time)

    def t_right(self, speed, t_time=0):
        self.L_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.AIN2, False)  # AIN2
        GPIO.output(self.AIN1, True)  # AIN1

        self.R_Motor.ChangeDutyCycle(speed)
        GPIO.output(self.BIN2, True)  # BIN2
        GPIO.output(self.BIN1, False)  # BIN1
        time.sleep(t_time)
