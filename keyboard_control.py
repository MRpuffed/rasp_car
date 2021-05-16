#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 8:05 下午
# @Author  : Dynasty
# @File    : basic_control.py
# @Software: PyCharm
import RPi.GPIO as GPIO
from basic_control import BasicControl


class KeyboardControl(object):
    @staticmethod
    def pygame_key_event(speed):
        pygame.init()
        pygame.display.set_mode((640, 480))
        base_control = BasicControl()
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_UP:
                            base_control.t_up(speed)
                        elif event.key == K_DOWN:
                            base_control.t_down(speed)
                        elif event.key == K_LEFT:
                            base_control.t_left(speed)
                        elif event.key == K_RIGHT:
                            base_control.t_right(speed)
                        elif event.key == K_SPACE:
                            base_control.t_stop()
        except KeyboardInterrupt:
            GPIO.cleanup()


if __name__ == "__main__":
    import pygame
    from pygame.locals import *
    t_speed = 30
    KeyboardControl().pygame_key_event(t_speed)
