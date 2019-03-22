# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
from PCA9685ROBOT import PCA9685ROBOT
from PCA9685ROBOT import ROVER
from PCA9685ROBOT import MOTOR

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685ROBOT()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_med = 600  # Max pulse length out of 4096
servo_max = 2000

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


fwd_rht = MOTOR(4, 5, 6)
fwd_lft = MOTOR(9, 8, 7)
bwd_rht = MOTOR(10, 11, 12)
bwd_lft = MOTOR(15, 14, 13)

rover = ROVER()

print('Moving servo on channel 0, press Ctrl-C to quit...')
try:
    while True:        
        # Move Rover Forward
        rover.stop_rover()
        time.sleep(2)

        rover.start_rover()
        time.sleep(2)
        rover.forward_rover()
        time.sleep(2)
        rover.stop_rover()
        time.sleep(2)

        # Move Rover Backward
        rover.start_rover()
        time.sleep(2)
        rover.reverse_rover()
        time.sleep(2)
        rover.stop_rover()
        time.sleep(2)

        # Move  Rover Speed
        rover.start_rover()
        time.sleep(2)
        rover.forward_rover()
        time.sleep(2)
        
        # Increase Rover Speed
        rover.set_rover_speed(60.5)        
        time.sleep(2)
        # Increase Rover Speed again
        rover.set_rover_speed(90.5)        
        time.sleep(2)

        # Decrease Rover Speed
        rover.set_rover_speed(50.5)        
        time.sleep(2)
        # Decrease Rover Speed again
        rover.set_rover_speed(10.5)        
        time.sleep(2)

        # Stop Rover
        rover.stop_rover()
        time.sleep(2)

        #pwm.set_pwm(0, 0, servo_min)
        #time.sleep(2)
        #pwm.set_pwm(0,0, servo_med)
        #time.sleep(2)
        #pwm.set_pwm(0, 0, servo_max)
        #time.sleep(5)

except KeyboardInterrupt:
    print('Attempt Program interrupt')
    rover.stop_rover()
    print('Program interrupted')
