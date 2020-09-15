#!/usr/bin/env python3
# license removed for brevity
import rospy
from lattepanda_behaviours.msg import vect_msg
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111, projection='polar')
ax.grid(True)
ax.set_title("Polar vector plot", va='bottom')

def plot_des_vect():

    # Intialize node and topic
    rospy.init_node('plot_vectors', anonymous=False)
    nvect = 4
    r = np.linspace(0,1,nvect)
    g = np.roll(r,1) 
    b = np.roll(g,1)
    
    while True:
        nav = rospy.wait_for_message('navigator_vect',vect_msg)        
        mic = rospy.wait_for_message('microphone_vect',vect_msg)
        rs = rospy.wait_for_message('rs_vect',vect_msg)
        bb = rospy.wait_for_message('behaviour_vect',vect_msg)

        # rospy.loginfo(nav)
        # rospy.loginfo(mic)
        # rospy.loginfo(rs)
        # rospy.loginfo(bb)

        ax.clear()
        RMAX = 5
        ax.set_rmax(RMAX)

        color = (r[0], g[0], b[0])
        plt.arrow(nav.angle*np.pi/180, 0, 0, nav.value, alpha = 0.5, width = 0.015,edgecolor = color, facecolor = color, lw = 2, zorder = 5)
        color = (r[1], g[1], b[1])
        plt.arrow(bb.angle*np.pi/180, 0, 0, bb.value, alpha = 0.5, width = 0.015,edgecolor = color, facecolor = color, lw = 2, zorder = 5)
        color = (r[2], g[2], b[2])
        plt.arrow(rs.angle*np.pi/180, 0, 0, rs.value, alpha = 0.5, width = 0.015,edgecolor = color, facecolor = color, lw = 2, zorder = 5)
        color = (r[3], g[3], b[3])
        plt.arrow(mic.angle*np.pi/180, 0, 0, mic.value, alpha = 0.5, width = 0.015,edgecolor = color, facecolor = color, lw = 2, zorder = 5)
    
        plt.show(block=False)
        plt.pause(0.001)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        plot_des_vect()
    except rospy.ROSInterruptException:
        pass
