#!/usr/bin/env python
# license removed for brevity
import rospy
from lattepanda_behaviours.msg import vect_msg
import numpy
import message_filters
import vector_fcn as vectfcn
import os
os.environ['MAVLINK20']='1' #set mavlink2 for odometry message
from pymavlink import mavutil
# from drawnow import drawnow, figure
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

connection = mavutil.mavlink_connection("udp:192.168.1.10:8150",input=False)
msg = vect_msg()

# Initialize the graph
fig = plt.figure(1)
ax = plt.subplot(111, projection='polar')

RMAX = 4
ax.set_rmax(RMAX)
ax.grid(True)
ax.set_title("Polar vector plot", va='bottom')
l, = ax.plot([],[])

vect = [[0,0]] 

# TODO define mavlink message to send a vector instead of Odometry Msg 
def update(i):
    global vect
    # vectfcn.plt_vect(vect)
    datay = random.random()
    l.set_data(2, datay)
    return l,


def callback(nav_sub,mic_sub,rs_sub,pub):
    global vect
    # Collecting vectors
    vect_a  = [mic_sub.angle, mic_sub.value]
    vect_b  = [nav_sub.angle, nav_sub.value]
    vect_c  = [rs_sub.angle, rs_sub.value]

    # Sum vectors
    bb_vect = vectfcn.sum_vect(vectfcn.sum_vect(vect_a,vect_b),vect_c)
    vect = [vect_a,vect_b,vect_c,bb_vect]
    # drawnow(vectfcn.plt_vect,[vect_b])
    # vectfcn.plt_vect()
    rospy.loginfo(bb_vect) 
    
    # Preparing Mavlink Odometry Msg
    time_usec = 0
    frame_id = 0
    child_frame_id = 0
    x = bb_vect[0]
    y = bb_vect[1]
    z = 0
    q = [0,0,0,0]
    vx = 0
    vy = 0
    vz = 0
    rollspeed = 0
    pitchspeed = 0
    yawspeed = 0
    pose_covariance=[]
    velocity_covariance=[]    
    for i in range (21): 
        pose_covariance.append(0)
        velocity_covariance.append(0)
    reset_counter=0
    estimator_type=0

    # Sending Mavlink Msg
    connection.mav.odometry_send(time_usec,frame_id,child_frame_id,x,y,z,q,vx,vy,vz,rollspeed,pitchspeed,yawspeed,pose_covariance,velocity_covariance,reset_counter,estimator_type)
    msg.angle = bb_vect[0]
    msg.value = bb_vect[1]
    pub.publish(msg)

def behaviour_main():
    # Intialize node and topic
    pub = rospy.Publisher('behaviour_vect', vect_msg, queue_size=100)
    rospy.init_node('behaviour_ros', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    ani = animation.FuncAnimation(fig,update,frames=50,interval=200,blit=True)
    plt.show(block=False)
    # Initialize ros message
    # msg = vect_msg()
    # Initialize mavlink connection to K64F board
    # Subscribe to messages
    rs_sub = message_filters.Subscriber('/rs_vect', vect_msg)
    mic_sub = message_filters.Subscriber('/microphone_vect', vect_msg)
    nav_sub = message_filters.Subscriber('/navigator_vect', vect_msg)
    # Syncronize
    ts = message_filters.ApproximateTimeSynchronizer([nav_sub,mic_sub,rs_sub], queue_size=10, slop=0.5)
    # Run callback
    ts.registerCallback(callback,pub)
    rospy.spin()           


if __name__ == '__main__':
    try:
        behaviour_main()
    except rospy.ROSInterruptException:
        pass