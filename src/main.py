#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from push_back.events import *

# Open log based on config
config_open_log()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(1200, 1200))
    reset_heading_to_aim(Position(1250, 1200), FORWARD)
    # reset_robot_position_and_heading_to_gps()

    # robot should be 77.5 cm from both sides

    matchload.set(True)
    trigger_mover.move(Position(1250, 1200), FORWARD)

    conveyor.front_motor.spin(FORWARD)
    conveyor.back_motor.spin(FORWARD)
    conveyor.top_motor.spin(FORWARD)
    wait(6000, MSEC)
    conveyor.front_motor.stop()
    conveyor.back_motor.stop()
    conveyor.top_motor.stop()

    # trigger_mover.move(Position(1200, 1200), REVERSE)
    # trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    # slow_trigger_mover.move(Position(800, 1200), FORWARD)

    # conveyor.front_motor.spin(REVERSE)
    # conveyor.back_motor.spin(REVERSE)
    # conveyor.top_motor.spin(FORWARD)
    # wait(6000, MSEC)

    # robot_position.reset(Position(1500, 1200))
    # reset_heading_to_aim(Position(600, 600), REVERSE)

    # reset_robot_position_and_heading_to_gps()

    # slow_trigger_mover.move(Position(600, 600), REVERSE)
    # wait_and_clamp()
    # intake.spin_forward()

    # # Use this for 4-ring
    # trigger_mover.move(Position(600, 1200))
    # trigger_mover.move(Position(240, 1210))
    # trigger_mover.move(Position(600, 1200), REVERSE)
    # trigger_mover.move(Position(240, 1100))
    # wait(1500, MSEC)
    # trigger_mover.move(Position(305, 353))
    # unclamp()
    # intake.stop()

    # Use this for 2-ring
    # trigger_turner.turn(42, FRAME_ABSOLUTE)
    # intake.spin_forward()
    # trigger_mover.move(Position(-350, 1000))
    # unclamp()

    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
