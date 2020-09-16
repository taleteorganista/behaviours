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

# BH1750 (GY-30) address 
# Detail on 
bh1750_address = 0x23
bh1750_power_on = 0x01
bh1750_resolution = 0x10
bh1750_factor = 1.2
reg = None
nbytes = 2
lux = 0

def compute_lux(data):
    global lux
    high = bin(data[3])[2:]
    low = bin(data[4])[2:]
    lux = float(int(high+low,2))/bh1750_factor

def light():
    # Intialize node and topic
     # Intialize node and topic
    pub = rospy.Publisher('light_vect', vect_msg, queue_size=10)
    rospy.init_node('light_behaviour', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = vect_msg()

    # Initialize i2c with pymata 
    board = pymata4.Pymata4()
    board.set_pin_mode_i2c()
    board.i2c_write(bh1750_address,[bh1750_power_on])
    board.i2c_write(bh1750_address,[bh1750_resolution])
    
    angle = 0 
        
    while not rospy.is_shutdown():
        board.i2c_read(address=bh1750_address,register=None,number_of_bytes=nbytes,callback=compute_lux)
        time.sleep(0.2)

        #TODO define here a behavior according to the lux value
        
        # Fill vector message
        msg.angle = angle
        msg.value = lux
        msg.header.stamp = rospy.Time.now()
        rospy.loginfo('Light vector data sent')
        pub.publish(msg)
        rate.sleep()

    
if __name__ == '__main__':
    try:
        light()
    except rospy.ROSInterruptException:
        pass