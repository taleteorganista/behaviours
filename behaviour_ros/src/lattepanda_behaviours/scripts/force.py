#!/usr/bin/env python3
# license removed for brevity

# For details of GY30 (BH1750)
# go to https://gist.github.com/Koepel/b70f81c71a52d8d6d3da86b9fe56d50e

import rospy
from lattepanda_behaviours.msg import vect_msg
from pymata4 import pymata4
#from pyfirmata import Arduino, util
import time
import numpy as np

sensor_pin_left = 0
sensor_pin_right = 1

def force():
    # Intialize node and topic
     # Intialize node and topic
    pub = rospy.Publisher('force_vect', vect_msg, queue_size=10)
    rospy.init_node('force_behaviour', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = vect_msg()

    # Initialize i2c with pymata 
    board = pymata4.Pymata4()
    board.set_pin_mode_analog_input(pin_number=sensor_pin_left)
    board.set_pin_mode_analog_input(pin_number=sensor_pin_right)
    
    angle = 0. 
    force = 0.
    while not rospy.is_shutdown():
        forceL = (float(board.analog_read(sensor_pin_left)[0]))
        forceR = (float(board.analog_read(sensor_pin_right)[0]))
        time.sleep(0.2)

        #TODO define here a behavior according to the lux value
        angle = (forceL - forceR) * 180/1023
        force = (forceL+forceR)/2

        # Fill vector message
        msg.angle = angle
        msg.value = force
        msg.header.stamp = rospy.Time.now()
        # rospy.loginfo('Force vector data sent')
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        force()
    except rospy.ROSInterruptException:
        pass