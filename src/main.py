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

    robot_position.reset(Position(1200, 1185))
    reset_heading_to_aim(Position(1480, 1185), FORWARD)


    matchload.set(True)

    wait(1000, MSEC)

    flap.set(True)

    wait(1000, MSEC)

    conveyor.spin(REVERSE, FORWARD, FORWARD)

    # trigger_mover.move(Position(1480, 1185), FORWARD)
    trigger_driver.drive(260)
    # trigger_driver.drive(-50)
    # wait(100, MSEC)
    # trigger_driver.drive(70)
    matchload.set(False)
    wait(220, MSEC)
    matchload.set(True)

    wait(200, MSEC)
    # conveyor.spin(STOP, STOP, STOP)
    # flap.set(False)

    trigger_mover.move(Position(1200, 1200), REVERSE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    matchload.set(False)
    trigger_turner.turn(177, FRAME_HEADING_RELATIVE)
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)

    trigger_mover.move(Position(900, 1200), FORWARD)
    # trigger_turner.turn(270, FRAME_ABSOLUTE) # do another check
    conveyor.spin(REVERSE, FORWARD, FORWARD)





    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
