# complete implementation of script found in test/test.py
from pylab import *
from drawnow import drawnow, figure
import numpy as np
# if global namespace, import plt.figure before drawnow.figure

def approx(x, k):
    """Approximate x with k singular values"""
    ...

figure(figsize=(7, 7/2))
def draw_fig():
    subplot(1, 2, 1)
    plt.(x)

    subplot(1, 2, 2)
    imshow(x)
    #show()

x = np.linspace(0,10,9)
drawnow(draw_fig)