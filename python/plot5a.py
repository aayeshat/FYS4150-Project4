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
e24_ordered = np.loadtxt("../out/data/energy_T2.4_ordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
e24_unordered = np.loadtxt("../out/data/energy_T2.4_unordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)

m_ordered = np.loadtxt("../out/data/magnetization_T1.0_ordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
m_unordered = np.loadtxt("../out/data/magnetization_T1.0_unordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
m24_ordered = np.loadtxt("../out/data/magnetization_T2.4_ordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)
m24_unordered = np.loadtxt("../out/data/magnetization_T2.4_unordered_problem5.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)

plt.figure()
plt.plot(mc, e_ordered, label="ordered", color="b")
plt.plot(mc, e_unordered, label="unordered", color="r")
plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("MC_cycles")
plt.ylabel("Energy per spins")
plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot/5a_energy_T1.0.pdf")

plt.figure()
plt.plot(mc, e24_ordered, label="ordered", color="b")
plt.plot(mc, e24_unordered, label="unordered", color="r")
plt.legend()
plt.title("T=2.4 [J/$k_b$] L=20")
plt.xlabel("MC_cycles")
plt.ylabel("Energy per spins")
plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot/5a_energy_T2.4.pdf")


plt.figure()
plt.plot(mc, m_ordered, label="ordered", color="b")
plt.plot(mc, m_unordered, label="unordered", color="r")
plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("MC_cycles")
plt.ylabel("Magnetization per spins")
plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot/5a_magnetization_T1.0.pdf")

plt.figure()
plt.title("T=2.4 [J/$k_b$] L=20")
plt.plot(mc, m24_ordered, label="ordered", color="b")
plt.plot(mc, m24_unordered, label="unordered", color="r")
plt.legend()
plt.title("T=2.4 [J/$k_b$] L=20")
plt.xlabel("MC_cycles")
plt.ylabel("Magnetization per spins")
plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot/5a_magnetization_T2.4.pdf")
