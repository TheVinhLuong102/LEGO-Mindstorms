#!/usr/bin/env micropython


from ev3dev2.motor import (
    LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
)
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.display import Display
from ev3dev2.sound import Sound


class EV3Game:
    def __init__(
            self,
            b_motor_port: str = OUTPUT_B, c_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.b_motor = LargeMotor(address=b_motor_port)
        self.c_motor = LargeMotor(address=c_motor_port)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.console = Console()
        self.screen = Display()
        self.speaker = Sound()

        self.offset_holdcup = 60
        self.current_b = self.current_c = 1

    def move_1_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = 2 * self.offset_holdcup + 180

        elif self.current_b == 3:
            self.rotate_b = 180

    def move_1_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_2_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = -180

        elif self.current_b == 3:
            self.rotate_b = 2 * self.offset_holdcup + 180

    def move_2_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_3_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_3_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 180

        elif self.current_c == 3:
            self.rotate_c = 2 * self.offset_holdcup + 180

    def move_4_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_4_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 2 * self.offset_holdcup + 180

        elif self.current_c == 3:
            self.rotate_c = -180
