#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop

from random import randint
from time import sleep


class EV3Game(EV3Brick):
    def __init__(
            self,
            b_motor_port: Port = Port.B, c_motor_port: Port = Port.C,
            grip_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.b_motor = Motor(port=b_motor_port,
                             positive_direction=Direction.CLOCKWISE)
        self.c_motor = Motor(port=c_motor_port,
                             positive_direction=Direction.CLOCKWISE)

        self.grip_motor = Motor(port=grip_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def start_up(self):
        self.light.on(color=Color.RED)

        self.calibrate_grip()

        self.screen.clear()

        self.level = 1

        self.display_level()

        self.choice = 2

        self.display_cup_number()

        self.offset_holdcup = 60
        self.current_b = self.current_c = 1

    def calibrate_grip(self):
        self.grip_motor.run(speed=-100)

        sleep(0.5)

        self.grip_motor.run_until_stalled(
            speed=-100,
            then=Stop.HOLD,
            duty_limit=None)

        self.grip_motor.run_angle(
            speed=100,
            rotation_angle=30,
            then=Stop.HOLD,
            wait=True)

    def display_level(self):
        ...

    def display_cup_number(self):
        ...

    def select_level(self):
        ...

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

    def execute_move(self):
        ...

    def update_ballcup(self):
        ...

    def shuffle(self):
        for _ in range(15):
            move = randint(1, 4)

            if move == 1:
                self.move_1_rotate_b()
                self.move_1_rotate_c()

                self.current_b = 3
                self.current_c = 1

            elif move == 2:
                self.move_2_rotate_b()
                self.move_2_rotate_c()

                self.current_b = 2
                self.current_c = 1

            elif move == 3:
                self.move_3_rotate_b()
                self.move_3_rotate_c()

                self.current_b = 1
                self.current_c = 2

            elif move == 4:
                self.move_4_rotate_b()
                self.move_4_rotate_c()

                self.current_b = 1
                self.current_c = 3

            self.execute_move()

            self.update_ballcup()

    def select_choice(self):
        ...

    def cup_to_center(self):
        ...

    def main(self):
        self.start_up()

        while True:
            self.cup_with_ball = 2

            self.select_level()

            self.light.on(color=Color.GREEN)

            self.shuffle()

            self.move_3_rotate_b()

            self.move_1_rotate_c()

            self.current_b = self.current_c = 1

            self.execute_move()

            self.light.off()

            correct_choice = False

            while not correct_choice:
                self.select_choice()

                self.cup_to_center()

                self.grip_motor.run_angle(
                    speed=100,
                    rotation_angle=220,
                    then=Stop.HOLD,
                    wait=True)

                correct_choice = (self.cup_with_ball == 2)

                if correct_choice:
                    self.light.on(color=Color.GREEN)

                    self.speaker.play_file(file=SoundFile.CHEERING)

                else:
                    self.light.on(color=Color.RED)

                    self.speaker.play_file(file=SoundFile.BOO)

            sleep(2)

            self.calibrate_grip()


if __name__ == '__main__':
    EV3_GAME = EV3Game()

    EV3_GAME.main()
