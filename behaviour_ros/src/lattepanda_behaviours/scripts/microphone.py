#!/usr/bin/env python3
# license removed for brevity
import rospy
from lattepanda_behaviours.msg import vect_msg
from std_msgs.msg import Int16MultiArray
import numpy as np
import time



def callback(data):
    SampleWin = 0.25
    SignalMinL = 1.0
    SignalMaxL = 0.0
    SignalMinR = 1.0
    SignalMaxR = 0.0
    threshold = 0.7
    msg = vect_msg()
    pub = rospy.Publisher('mic_vect', vect_msg, queue_size=10)
    start = time.time()
    while(time.time() - start)< SampleWin:
        valL = float (data.data[0]/1024.0)  # Read left mic            
        valR = float (data.data[1]/1024.0) # Read left mic
        
        if (valL) == None:
            rospy.logwarn("Left Mic acquisition failed")
            valL=0
        if (valR) == None:
            rospy.logwarn("Right Mic acquisition failed")
            valR=0
        # Processing left mic
        if(valL > SignalMaxL):
            SignalMaxL = valL
        elif valL < SignalMinL:
            SignalMinL = valL
        # Processing right mic
        if(valR > SignalMaxR):
            SignalMaxR = valR
        elif valR < SignalMinR:
            SignalMinR = valR
        
    pktopkL = valL
    pktopkR = valR
    # rospy.loginfo(pktopkL)
    
    if (SignalMaxL > threshold or SignalMaxR > threshold):
        value = 1
    else:
        value = 0

    if pktopkL > 0.65:   
        rospy.loginfo('Left Calmp')
    SignalMinL = 1.0
    SignalMaxL = 0.0
    
    if pktopkR > 0.65:
        rospy.loginfo('Right Calmp')
    SignalMinR = 1.0
    SignalMaxR = 0.0
    angle=(pktopkL - pktopkR)*180/np.pi

    msg.angle = angle
    msg.value = value
    msg.header.stamp = rospy.Time.now()
    pub.publish(msg)
    rospy.loginfo('Microphone vector sent')
    
def microphone():
    # Intialize node and topic
    rospy.init_node('microphone_behaviour', anonymous=True)
    rospy.Subscriber("mic_data", Int16MultiArray, callback)
    rospy.spin()
        
if __name__ == '__main__':
    try:
        microphone()
    except rospy.ROSInterruptException:
        pass
