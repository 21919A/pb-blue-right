#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from push_back.events import *

# Open log based on config
config_open_log()

calibrate_and_wait()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(1250, 380))
    reset_heading_to_aim(Position(1250, 1200), FORWARD)

    # robot_position.reset(Position(1600, 450))
    # reset_heading_to_aim(Position(900, 450), FORWARD)
    flap.set(True)
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)

    trigger_mover.move(Position(1250, 1200), FORWARD)
    # trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)

    trigger_driver.drive_for_time(1000, 20, True, 243)
    trigger_driver.drive(-35)

    wait(755, MSEC)

    trigger_mover.move(Position(1200, 1200), REVERSE)
    flap.set(False)
    matchload.set(False)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    conveyor.spin(STOP, STOP, STOP)
    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    trigger_mover.move(Position(900, 1200))
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
