from queue import Queue

def intialize_global_vars():
    global queue_rs
    global queue_mic 
    global queue_nav

    queue_rs = Queue(2)
    queue_mic = Queue(2)
    queue_nav = Queue(2)
    queue_rs.put([0, 0])
    queue_mic.put([0, 0])
    queue_nav.put([0, 0])
    