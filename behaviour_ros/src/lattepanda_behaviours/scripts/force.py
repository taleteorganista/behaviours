#!/usr/bin/env python3
# license removed for brevity

# For details of GY30 (BH1750)
# go to https://gist.github.com/Koepel/b70f81c71a52d8d6d3da86b9fe56d50e

import rospy
from lattepanda_behaviours.msg import vect_msg
from std_msgs.msg import Int16MultiArray 

def callback(data):
    angle = 0. 
    force = 0.
    msg = vect_msg()
    forceL = data.data[0]
    forceR = data.data[1]

    #TODO define here a behavior according to the lux value
    angle = (forceL - forceR) * 180/1023
    force = (forceL+forceR)/2

    # Fill vector message
    msg.angle = angle
    msg.value = force
    msg.header.stamp = rospy.Time.now()
    pub = rospy.Publisher('force_vect', vect_msg, queue_size=10)
    pub.publish(msg)
    rospy.loginfo('Force vector sent')

def force():   
    rospy.init_node('force_behaviour', anonymous=True)
    rospy.Subscriber("force_data", Int16MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        force()
    except rospy.ROSInterruptException:
        pass