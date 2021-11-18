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

basepath = "../out/data_8";
T = np.loadtxt(basepath + "/energy_L20_ordered_problem8.txt", dtype="double", usecols = (0), unpack = True, skiprows = 0)

exp_E_ordered_20, exp_M_ordered_20, C_v_ordered_20, X_ordered_20 = np.loadtxt(basepath +"/energy_L20_ordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_ordered_40, exp_M_ordered_40, C_v_ordered_40, X_ordered_40 = np.loadtxt(basepath +"/energy_L40_ordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_ordered_80, exp_M_ordered_80, C_v_ordered_80, X_ordered_80 = np.loadtxt(basepath +"/energy_L80_ordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_ordered_100, exp_M_ordered_100, C_v_ordered_100, X_ordered_100 = np.loadtxt(basepath +"/energy_L100_ordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)


exp_E_unordered_20, exp_M_unordered_20, C_v_unordered_20, X_unordered_20 = np.loadtxt(basepath +"/energy_L20_unordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_unordered_40, exp_M_unordered_40, C_v_unordered_40, X_unordered_40 = np.loadtxt(basepath +"/energy_L40_unordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_unordered_80, exp_M_unordered_80, C_v_unordered_80, X_unordered_80 = np.loadtxt(basepath +"/energy_L80_unordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_unordered_100, exp_M_unordered_100, C_v_unordered_100, X_unordered_100 = np.loadtxt(basepath +"/energy_L100_unordered_problem8.txt", dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)

##exp_E

plt.figure()
plt.plot(T, exp_E_ordered_20, label="ordered L20", color="b")
plt.plot(T, exp_E_ordered_40, label="ordered L40", color="g")
plt.plot(T, exp_E_ordered_80, label="ordered L80", color="r")
plt.plot(T, exp_E_ordered_100, label="ordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("exp_E")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_ordered_exp_E.pdf")

plt.figure()
plt.plot(T, exp_E_unordered_20, label="unordered L20", color="b")
plt.plot(T, exp_E_unordered_40, label="unordered L40", color="g")
plt.plot(T, exp_E_unordered_80, label="unordered L80", color="r")
plt.plot(T, exp_E_unordered_100, label="unordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("exp_E")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_unordered_exp_E.pdf")

##exp_M

plt.figure()
plt.plot(T, exp_M_ordered_20, label="ordered L20", color="b")
plt.plot(T, exp_M_ordered_40, label="ordered L40", color="g")
plt.plot(T, exp_M_ordered_80, label="ordered L80", color="r")
plt.plot(T, exp_M_ordered_100, label="ordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("exp_M")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_ordered_exp_M.pdf")

plt.figure()
plt.plot(T, exp_M_unordered_20, label="unordered L20", color="b")
plt.plot(T, exp_M_unordered_40, label="unordered L40", color="g")
plt.plot(T, exp_M_unordered_80, label="unordered L80", color="r")
plt.plot(T, exp_M_unordered_100, label="unordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("exp_M")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_unordered_exp_M.pdf")

##C_v

plt.figure()
plt.plot(T, C_v_ordered_20, label="ordered L20", color="b")
plt.plot(T, C_v_ordered_40, label="ordered L40", color="g")
plt.plot(T, C_v_ordered_80, label="ordered L80", color="r")
plt.plot(T, C_v_ordered_100, label="ordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("C_v")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_ordered_C_v.pdf")

plt.figure()
plt.plot(T, C_v_unordered_20, label="unordered L20", color="b")
plt.plot(T, C_v_unordered_40, label="unordered L40", color="g")
plt.plot(T, C_v_unordered_80, label="unordered L80", color="r")
plt.plot(T, C_v_unordered_100, label="unordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("C_v")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_unordered_C_v.pdf")



##X

plt.figure()
plt.plot(T, X_ordered_20, label="ordered L20", color="b")
plt.plot(T, X_ordered_40, label="ordered L40", color="g")
plt.plot(T, X_ordered_80, label="ordered L80", color="r")
plt.plot(T, X_ordered_100, label="ordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("X")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_ordered_X.pdf")

plt.figure()
plt.plot(T, X_unordered_20, label="unordered L20", color="b")
plt.plot(T, X_unordered_40, label="unordered L40", color="g")
plt.plot(T, X_unordered_80, label="unordered L80", color="r")
plt.plot(T, X_unordered_100, label="unordered L100", color="k")

plt.legend()
plt.title("T=1.0 [J/$k_b$] L=20")
plt.xlabel("T")
plt.ylabel("X")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_energy_unordered_X.pdf")
