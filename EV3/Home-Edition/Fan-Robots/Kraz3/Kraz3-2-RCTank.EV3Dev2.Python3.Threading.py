#!/usr/bin/env python3

"""
Add the Kung-Fu Maneouver
via the Touch Sensor and Remote Control of head and arms
"""

from kraz3_rctank_ev3dev2 import Kraz3

from threading import Thread


KRAZ3 = Kraz3()


Thread(
    target=KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled,
    daemon=True).start()

KRAZ3.main()
