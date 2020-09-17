#!/usr/bin/env python3
# license removed for brevity

# For details of GY30 (BH1750)
# go to https://gist.github.com/Koepel/b70f81c71a52d8d6d3da86b9fe56d50e

import rospy
from lattepanda_behaviours.msg import vect_msg
from std_msgs.msg import Int16MultiArray
bh1750_factor = 1.2
bh1750_max_lux = 54612

def compute_lux(data_light):
    high = bin(data_light[0])[2:]
    low = bin(data_light[1])[2:]
    lux = (float(int(high+low,2))/bh1750_factor)/bh1750_max_lux
    return(lux)

def callback(data):
    data_light = [data.data[0], data.data[1]]
    lux = compute_lux(data_light)
    msg = vect_msg()

    #TODO define here a behavior according to the lux value
    angle = 0
    # Fill vector message
    msg.angle = angle
    msg.value = lux
    msg.header.stamp = rospy.Time.now()
    pub = rospy.Publisher('light_vect', vect_msg, queue_size=10)
    pub.publish(msg)
    rospy.loginfo('Light vector sent')

def light():
    rospy.init_node('light_behaviour', anonymous=True)
    rospy.Subscriber("light_data", Int16MultiArray, callback)
    rospy.spin()
       
if __name__ == '__main__':
    try:
        light()
    except rospy.ROSInterruptException:
        pass