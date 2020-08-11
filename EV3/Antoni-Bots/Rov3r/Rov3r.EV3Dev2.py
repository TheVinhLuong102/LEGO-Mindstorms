#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound



import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Rov3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            gear_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.gear_motor = MediumMotor(address=gear_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.speaker = Sound()
        self.dis = Display(desc='Display')


    def spin_gears(self, speed: float = 100):
        if self.ir_sensor.beacon(channel=1):
            self.gear_motor.on(
                speed=speed,
                block=False,
                brake=False)

        else:
            self.gear_motor.off(brake=True)


    def change_screen_when_touched(self):
        if self.touch_sensor.is_pressed:
            self.dis.image_filename(
                filename='/home/robot/image/Angry.bmp',
                clear_screen=True)
            self.dis.update()

        else:
            self.dis.image_filename(
                filename='/home/robot/image/Fire.bmp',
                clear_screen=True)
            self.dis.update()


    def make_noise_when_seeing_black(self):
        if self.color_sensor.color == ColorSensor.COLOR_BLACK:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Ouch.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)


    def main(self):
        self.speaker.play_file(
            wav_file='/home/robot/sound/Yes.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        while True:
            self.dis.image_filename(
                filename='/home/robot/image/Fire.bmp',
                clear_screen=True)
            self.dis.update()

            self.drive_once_by_ir_beacon(speed=100)

            self.make_noise_when_seeing_black()

            self.spin_gears(speed=100)

            self.change_screen_when_touched()


if __name__ == '__main__':
    ROV3R = Rov3r()

    ROV3R.main()