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

mc = np.loadtxt("../out/data/montecarlo_cycles.txt", dtype="double")


e_ordered = np.loadtxt("../out/data/energy_T1.0_ordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
e_unordered = np.loadtxt("../out/data/energy_T1.0_unordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)

plt.figure()
plt.plot(mc, e_ordered, label="T=1.0 ordered", color="b")
plt.plot(mc, e_unordered, label="T=1.0 unordered", color="c")
plt.legend()
plt.xlabel("MC_cycles")
plt.ylabel("<$ \epsilon$>")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/5a_T1.0_Energy.pdf")


# e24_ordered = np.loadtxt("../out/data/energy_T2.4_ordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
# e24_unordered = np.loadtxt("../out/data/energy_T2.4_unordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)

# plt.figure()
# plt.plot(mc, e24_ordered, label="T=2.4 ordered", color="b")
# plt.plot(mc, e24_unordered, label="T=2.4 unordered", color="r")
# plt.legend()
# plt.xlabel("MC_cycles")
# plt.ylabel("Energy per spins")
# plt.grid(linestyle = '--', linewidth = 0.2)
# plt.savefig("../out/5a_T2.4.pdf")