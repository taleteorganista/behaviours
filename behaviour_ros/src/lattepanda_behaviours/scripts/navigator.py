#!/usr/bin/env python3
# license removed for brevity
import rospy
from lattepanda_behaviours.msg import vect_msg
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
        value = 0.8
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
