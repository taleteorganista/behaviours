#!/usr/bin/env python
# license removed for brevity
import rospy
from lattepanda_behaviours.msg import vect_msg
from pyfirmata import Arduino, util
import time
import numpy

def navigator():
    # Intialize node and topic
    pub = rospy.Publisher('navigator_vect', vect_msg, queue_size=10)
    rospy.init_node('navigator_behaviour', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = vect_msg()

    while not rospy.is_shutdown():
        angle = 0
        value = 1.5
        vect = [angle,value]
        msg.header.stamp = rospy.Time.now()
        msg.angle = angle
        msg.value = value
        rospy.loginfo('Navigator vector data sent')
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        navigator()
    except rospy.ROSInterruptException:
        pass
