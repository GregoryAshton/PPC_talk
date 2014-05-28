import matplotlib.pyplot as plt
import numpy as np
import sys

import nsmod_one_component_model as NOCM
from Plotting import PlotFromFileName

file_name = NOCM.main()

if "simple" in sys.argv:
    [time, w1, w2, w3] = np.genfromtxt(file_name).T

    plt.plot(time, w1)
    plt.show()

if "all" in sys.argv:
    PlotFromFileName(file_name)

