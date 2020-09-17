#!/usr/bin/env python3
# license removed for brevity
import rospy
from pymata4 import pymata4
#from pyfirmata import Arduino, util
import time
import numpy as np
from std_msgs.msg import Int16MultiArray

#TODO check sensor range and normalization (in behaviours!)

# ANALOG Pin definition
# fsr 
fsr_left = 0    # Force Resistor Sensor / Left side 
fsr_right = 1   # Force Resistor Sensor / Right side
fsr = [fsr_left,fsr_right]
# mic
mic_left = 2    # Microphone Sensor     / Left side
mic_right = 3   # Microphone Snesor     / Right Side
mic = [mic_left,mic_right]
# analog pins
analog_pins = fsr + mic

# DIGITAL Pin defintion
led_status = 13 # Status led
status = False
digital_pins = [led_status]

# I2C definition
bh1750_address = 0x23
bh1750_power_on = 0x01
bh1750_resolution = 0x10
bh1750_factor = 1.2
nbytes = 2 
light = []

def ckb(data):
    global light
    light = []
    light.append(data[3])
    light.append(data[4])
    

def sensor_manager():
    global status, light
    # Intialize node and topic
    pub_light = rospy.Publisher('light_data', Int16MultiArray, queue_size=10)
    pub_force = rospy.Publisher('force_data', Int16MultiArray, queue_size=10)
    pub_mic = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)

    rospy.init_node('senor_manager', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    # msg = vect_msg()

    # Initialize Arduino Leoardo with pymata4 
    board = pymata4.Pymata4()

    # Initialize i2c 
    board.set_pin_mode_i2c()
    board.i2c_write(bh1750_address,[bh1750_power_on])
    board.i2c_write(bh1750_address,[bh1750_resolution])

    # Initialize input analog pins
    for pin in analog_pins:
        board.set_pin_mode_analog_input(pin_number=pin)
    
    # Initialize output digital pins
    for pin in digital_pins:
        board.set_pin_mode_digital_output(pin_number=pin)

    mic_msg = Int16MultiArray()
    fsr_msg = Int16MultiArray()
    light_msg = Int16MultiArray()

    # Get raw data from board
    while True:
        # mic data
        mic_val = []
        for pin in mic:
            mic_val.append(list(board.analog_read(pin)))
            time.sleep(0.01)
        mic_msg.data = [mic_val[0][0], mic_val[1][0]]
        pub_mic.publish(mic_msg)

        # fsr data
        fsr_val = []
        for pin in fsr:
            fsr_val.append(list(board.analog_read(pin)))
            time.sleep(0.01)
        fsr_msg.data = [fsr_val[0][0], fsr_val[1][0]]
        pub_force.publish(fsr_msg)

        # light
        board.i2c_read(address=bh1750_address,register=None,number_of_bytes=nbytes,callback=ckb)
        light_msg.data = light
        pub_light.publish(light_msg)
        time.sleep(0.2)

        # status led
        status = not status
        board.digital_write(led_status,status)
        
        rospy.loginfo('Sent data')
        rate.sleep()

if __name__ == '__main__':
    try:
        sensor_manager()
    except rospy.ROSInterruptException:
        pass
