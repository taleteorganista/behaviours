import os
os.environ['MAVLINK20']='1' #set mavlink2 
from pymavlink import mavutil

connection = mavutil.mavlink_connection("udp:localhost:14540",input=False,dialect = "standard")
# connection = mavutil.mavlink_connection("udp:192.168.1.10:8150",input=False)

#    print(pose_covariance)
def send_vector():
    yaw=180
    speed=5
    angle=1
    print("sending new vector")
    target_system =0
    target_component =0
    relyaw =0
    vehicle_throttle =0 
    connection.mav.command_long_send(target_system,
                                     target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_SET_YAW_SPEED, 
                                     0,yaw,speed,1,0,0,0,0)
if __name__ == '__main__':
    while(1):
        send_vector()
