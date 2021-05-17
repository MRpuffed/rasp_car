#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 8:05 下午
# @Author  : Dynasty
# @File    : basic_control.py
# @Software: PyCharm
import RPi.GPIO as GPIO
from infrared_avoid import InfraredAvoid


class Xbox360Control(object):
    @staticmethod
    def pygame_key_event(speed=20):
        pygame.init()
        pygame.joystick.init()
        base_control = InfraredAvoid()
        # 返回游戏杆的数量
        if pygame.joystick.get_count() == 1:
            # 若只连接了一个手柄，此处带入的参数一般都是0
            joystick = pygame.joystick.Joystick(0)
            # 手柄对象初始化
            joystick.init()
            # 获得 Joystick 操纵轴的数量
            joystick_axes_num = joystick.get_numaxes()
            # 获得 Joystick 上追踪球的数量
            joystick_balls_num = joystick.get_numballs()
            # 获得 Joystick 上按钮的数量
            joystick_buttons_num = joystick.get_numbuttons()
            # 获得 Joystick 上帽键的数量
            joystick_hats_num = joystick.get_numhats()
            print(joystick_axes_num, joystick_balls_num, joystick_buttons_num, joystick_hats_num)
            # print(6, 0, 11, 1)
            try:
                while True:
                    base_control.avoid_obstacle(speed)
                    for i in range(joystick_axes_num):
                        axis = joystick.get_axis(i)
                        if i == 1 and axis == -1.0:
                            print("Left up", axis)
                            base_control.t_up(speed)
                        if i == 1 and axis > 0.3:
                            print("Left down", axis)
                            base_control.t_down(speed)
                        if i == 0 and axis == -1.0:
                            print("Left left", axis)
                            base_control.t_left(30)
                        if i == 0 and axis > 0.3:
                            print("Left right", axis)
                            base_control.t_right(30)
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
                                base_control.t_left(40)
                            elif joystick.get_button(1) == 1:
                                print("right")
                                base_control.t_right(40)
                            elif joystick.get_button(4) == 1:
                                if speed != 10:
                                    speed -= 10
                            elif joystick.get_button(5) == 1:
                                if speed != 100:
                                    speed += 10
                            elif joystick.get_button(6) == 1:
                                base_control.t_stop()
            except KeyboardInterrupt:
                GPIO.cleanup()


if __name__ == "__main__":
    import pygame
    from pygame.locals import *
    Xbox360Control().pygame_key_event()
