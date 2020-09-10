#!/usr/bin/env python
# license removed for brevity
import rospy
# from std_msgs.msg import Float32MultiArray
from lattepanda_behaviours.msg import vect_msg
from pyfirmata import Arduino, util
import time
import numpy as np

def microphone():
    # Intialize node and topic
    pub = rospy.Publisher('microphone_vect', vect_msg, queue_size=10)
    rospy.init_node('microphone_behaviour', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = vect_msg()
    
    # Initialize pyfirmata and mic
    board = Arduino("/dev/ttyACM0")
    analog_0 = board.get_pin('a:0:i')       # Left mic
    analog_1 = board.get_pin('a:1:i')       # Right mic
    it = util.Iterator(board)
    it.start()
    analog_0.enable_reporting()
    analog_1.enable_reporting()


    SampleWin = 0.25
    SignalMinL = 1.0
    SignalMaxL = 0.0
    SignalMinR = 1.0
    SignalMaxR = 0.0
    threshold = 0.7

    valL = 0

    while not rospy.is_shutdown():
        
        start = time.time()
        board.digital[13].write(0)
        while(time.time() - start)< SampleWin:
            valL = analog_0.read()              # Read left mic
            time.sleep(0.001)
            valR = analog_1.read()              # Read left mic
            time.sleep(0.001)
            # os.system( 'clear' )
            # print(val)
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
            
        pktopkL = SignalMaxL - SignalMinL
        pktopkR = SignalMaxR - SignalMinR
        
        if (SignalMaxL > threshold or SignalMaxR > threshold):
            value = 1
        else:
            value = 0

        if pktopkL > 0.12:
            board.digital[13].write(1)
            time.sleep(0.2)
            rospy.loginfo('Left Calmp')
        SignalMinL = 1.0
        SignalMaxL = 0.0
            
        
        if pktopkR > 0.12:
            board.digital[13].write(1)
            time.sleep(0.2)
            rospy.loginfo('Right Calmp')
        SignalMinR = 1.0
        SignalMaxR = 0.0
        angle=(pktopkL - pktopkR)*180/np.pi

        # vect = [angle,value]  

        msg.angle = angle
        msg.value = value
        msg.header.stamp = rospy.Time.now()
        rospy.loginfo('Microphone vector data sent')
        pub.publish(msg)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        microphone()
    except rospy.ROSInterruptException:
        pass
