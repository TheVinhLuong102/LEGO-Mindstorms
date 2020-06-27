#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, INPUT_1, INPUT_3,
    Screen, Sound
)

from PIL import Image
from threading import Thread
from time import time


LEFT_FOOT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_FOOT_MOTOR = LargeMotor(address=OUTPUT_C)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

COLOR_SENSOR = ColorSensor(address=INPUT_3)
TOUCH_SENSOR = TouchSensor(address=INPUT_1)

SCREEN = Screen()
SPEAKER = Sound()


def run_away_whenever_dark():
    while True:
        if COLOR_SENSOR.ambient_light_intensity < 5:   # 15 not dark enough
            SCREEN.image.paste(
                im=Image.open('/home/robot/image/Middle left.bmp'),
                box=(0, 0))

            LEFT_FOOT_MOTOR.run_timed(
                speed_sp=-800,
                time_sp=1500,
                stop_action=Motor.STOP_ACTION_BRAKE)

            RIGHT_FOOT_MOTOR.run_timed(
                speed_sp=-1000,
                time_sp=1500,
                stop_action=Motor.STOP_ACTION_BRAKE)

            LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

            RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

            SCREEN.image.paste(
                im=Image.open('/home/robot/image/Middle right.bmp'),
                box=(0, 0))

            LEFT_FOOT_MOTOR.run_timed(
                speed_sp=-1000,
                time_sp=1500,
                stop_action=Motor.STOP_ACTION_BRAKE)

            RIGHT_FOOT_MOTOR.run_timed(
                speed_sp=1000,
                time_sp=1500,
                stop_action=Motor.STOP_ACTION_BRAKE)

            LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

            RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

        else:
            if time() % 3 < 1.5:
                LEFT_FOOT_MOTOR.run_forever(speed_sp=500)

                RIGHT_FOOT_MOTOR.run_forever(speed_sp=1000)

            else:
                LEFT_FOOT_MOTOR.run_forever(speed_sp=1000)

                RIGHT_FOOT_MOTOR.run_forever(speed_sp=500)             

            SCREEN.image.paste(
                im=Image.open('/home/robot/image/Awake.bmp'),
                box=(0, 0))


def laugh_whenever_touched():
    while True:
        if TOUCH_SENSOR.is_pressed:
            SPEAKER.play(wav_file='/home/robot/sound/Laughing 1.wav').wait()

            MEDIUM_MOTOR.run_to_rel_pos(
                position_sp=6 * 360,
                speed_sp=1000,
                stop_action=Motor.STOP_ACTION_BRAKE)


Thread(target=run_away_whenever_dark,
       daemon=True).start()

laugh_whenever_touched()
