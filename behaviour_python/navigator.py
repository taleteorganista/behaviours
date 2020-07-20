import numpy
import global_vars

def navigator_behaviour():
    while True:
        angle = 0
        value = 1.5
        vect = [angle,value]
        # Fill the rs_queue
        global_vars.queue_nav.put(vect)