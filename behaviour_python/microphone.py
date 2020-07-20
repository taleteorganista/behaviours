from pyfirmata import Arduino, util
import time
import matplotlib.pyplot as plt
import numpy
import os
import global_vars

def microphone_behaviour():
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

    # val = numpy.zeros(10000)
    valL = 0
    while(1):

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
                # print("Left Mic acquisition failed")
                valL=0
            if (valR) == None:
                # print("Right Mic acquisition failed")
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
            # print('Left Calmp')
        SignalMinL = 1.0
        SignalMaxL = 0.0
            
        
        if pktopkR > 0.12:
            board.digital[13].write(1)
            time.sleep(0.2)
            # print('Right Calmp')
        SignalMinR = 1.0
        SignalMaxR = 0.0
        angle=(pktopkL - pktopkR)*180

        vect = [angle,value]    
        # Fill the rs_queue
        global_vars.queue_mic.put(vect)

    # plt.plot(val,marker='.')
    # plt.show()