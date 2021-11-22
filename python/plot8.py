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

startPath = "../out/data_8/energy_parallel_Limtited_";
endPath= "_unordered_problem8.txt"

T = np.loadtxt(startPath + "L40" + endPath, dtype="double", usecols = (0), unpack = True, skiprows = 0)

exp_E_40, exp_M_40, C_v_40, X_40 = np.loadtxt(startPath + "L40" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_60, exp_M_60, C_v_60, X_60 = np.loadtxt(startPath + "L60" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_80, exp_M_80, C_v_80, X_80 = np.loadtxt(startPath + "L80" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_100, exp_M_100, C_v_100, X_100 = np.loadtxt(startPath + "L100" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)

##exp_E

plt.figure()
plt.plot(T, exp_E_40, label="L40", color="g")
plt.plot(T, exp_E_60, label="L60", color="b")
plt.plot(T, exp_E_80, label="L80", color="r")
plt.plot(T, exp_E_100, label="L100", color="k")

plt.legend()
plt.title("L=20 unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("exp_E")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_exp_E.pdf")

##exp_M

plt.figure()
plt.plot(T, exp_M_40, label="L40", color="g")
plt.plot(T, exp_M_60, label="L60", color="b")
plt.plot(T, exp_M_80, label="L80", color="r")
plt.plot(T, exp_M_100, label="L100", color="k")

plt.legend()
plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("exp_M")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_exp_M.pdf")

##C_v

plt.figure()
plt.plot(T, C_v_40, label="L40", color="g")
plt.plot(T, C_v_60, label="L60", color="b")
plt.plot(T, C_v_80, label="L80", color="r")
plt.plot(T, C_v_100, label="L100", color="k")

plt.legend()
plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("C_v")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_C_v.pdf")
plt.show()


##X

plt.figure()
plt.plot(T, X_60, label="L60", color="b")
plt.plot(T, X_40, label="L40", color="g")
plt.plot(T, X_80, label="L80", color="r")
plt.plot(T, X_100, label="L100", color="k")

plt.legend()
plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("X")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_X.pdf")
plt.show()
