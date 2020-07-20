import global_vars
import threading
import time
import realsense_depth_matrix
import microphone
import navigator
import vector_fcn as vectfcn
import os
os.environ['MAVLINK20']='1' #set mavlink2 for odometry message
from pymavlink import mavutil

# TODO correct sum vector rs module must be positive

# initialize global queues for Realsense and Microphone
global_vars.intialize_global_vars()

# Thread definition
realsense   = threading.Thread(target=realsense_depth_matrix.realsense_behaviour,name='realsense-thread')
microphone  = threading.Thread(target=microphone.microphone_behaviour,name='microphone-thread')
navigator   = threading.Thread(target=navigator.navigator_behaviour,name='navigator-thread')

# Thread start
realsense.start()
microphone.start()
navigator.start()

# Setup a mavlink connection to desired upd (localhost or k64f) 
#connection = mavutil.mavlink_connection("udp:localhost:14540",input=False)
connection = mavutil.mavlink_connection("udp:192.168.1.10:8150",input=False)

while True:
    # get vectors from modules
    rs = global_vars.queue_rs.get()
    mic = global_vars.queue_mic.get()
    nav = global_vars.queue_nav.get()
    # sum polar vector
    vect = vectfcn.sum_vect(rs,vectfcn.sum_vect(mic,nav))
    # vectfcn.plt_vect([rs,mic,nav,vect])
    vectfcn.send_vect(vect,connection)
    print("\033c")
    print(rs,mic,nav,vect)

