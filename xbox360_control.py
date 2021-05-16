#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 8:05 下午
# @Author  : Dynasty
# @File    : basic_control.py
# @Software: PyCharm
import RPi.GPIO as GPIO
import time
import pygame
pygame.init()


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

    def pygame_key_event(self, speed=20):
        pygame.joystick.init()
        # 返回游戏杆的数量
        if pygame.joystick.get_count() == 1:
            # 若只连接了一个手柄，此处带入的参数一般都是0
            joystick = pygame.joystick.Joystick(0)
            # 手柄对象初始化
            joystick.init()
            # 获得 Joystick 操纵轴的数量
            joystick_axes_num = joystick.get_numaxes()
            # 获得 Joystick 上追踪球的数量
            joystick_balls_num = joystick.get_numaxes()
            # 获得 Joystick 上按钮的数量
            joystick_buttons_num = joystick.get_numaxes()
            print(joystick_axes_num, joystick_balls_num, joystick_buttons_num)
            try:
                while True:
                    for i in range(joystick_axes_num):
                        axis = joystick.get_axis(i)
                        if i == 1 and axis == -1.0:
                            print("Left up", axis)
                            self.t_up(speed)
                        if i == 1 and axis > 0.3:
                            print("Left down", axis)
                            self.t_down(speed)
                        if i == 0 and axis == -1.0:
                            print("Left left", axis)
                            self.t_left(30)
                        if i == 0 and axis > 0.3:
                            print("Left right", axis)
                            self.t_right(30)
                        if i == 4 and axis == -1.0:
                            print("Right up", axis)
                            if speed != 100:
                                speed += 10
                        if i == 4 and axis > 0.3:
                            print("Right down", axis)
                            if speed != 10:
                                speed -= 10
                        if i == 3 and axis == -1:
                            print("Right left", axis)
                        if i == 3 and axis > 0.3:
                            print("Right right", axis)
                        if i == 2 and axis > 0.3:
                            print("LT", axis)
                        if i == 5 and axis > 0.3:
                            print("RT", axis)
                    for event in pygame.event.get():
                        # print(event.type)
                        # JOYBUTTONDOWN和JOYBUTTONUP分别为操作杆动作"按键按下"和"按键抬起"
                        if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                            # 0-A;1-B;2-X;3-Y;4-LB;5-RB;7-BACK
                            if joystick.get_button(3) == 1:
                                # 返回1为按下，0为抬起
                                if speed != 10:
                                    speed -= 10
                            elif joystick.get_button(0) == 1:
                                if speed != 100:
                                    speed += 10
                            elif joystick.get_button(2) == 1:
                                print("left")
                                self.t_left(40)
                            elif joystick.get_button(1) == 1:
                                print("right")
                                self.t_right(40)
                            elif joystick.get_button(4) == 1:
                                if speed != 10:
                                    speed -= 10
                            elif joystick.get_button(5) == 1:
                                if speed != 100:
                                    speed += 10
                            elif joystick.get_button(6) == 1:
                                self.t_stop()
            except KeyboardInterrupt:
                GPIO.cleanup()


if __name__ == "__main__":
    BasicControl().pygame_key_event()
