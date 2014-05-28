import matplotlib.pyplot as plt
import numpy as np

def PlotFromFileName(file_name):
    [t, w1, w2, w3] = np.genfromtxt(file_name).T
    
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=3)
    
    ax1.plot(t, w1)

    ax2.plot(t, w2)

    ax3.plot(t, w3)

    plt.show()
