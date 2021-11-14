import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 14
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
mpl.rcParams["legend.fontsize"] = 7.5
plt.rcParams["figure.figsize"] = (7, 5)

m = np.loadtxt("../out/data/montecarlo_cycles.txt", dtype="double")
e = np.loadtxt("../out/data/energy_problem5.txt", dtype="double")

plt.plot(m, e)

plt.xlabel("MC_cycles")
plt.ylabel("Energy per spins")

plt.grid(linestyle = '--', linewidth = 0.2)

plt.savefig("../out/5a.pdf")