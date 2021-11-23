import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 14
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
mpl.rcParams["legend.fontsize"] = 7.5
plt.rcParams["figure.figsize"] = (7,5)

startPath = "../out/data_8/energy_";
endPath= "_unordered_problem8.bin"
endPath2 = "_unordered_limitedT.txt"

T = np.loadtxt(startPath + "L40" + endPath, dtype="double", usecols = (0), unpack = True, skiprows = 0)

#Text files with less data points/time steps = 0.05

exp_E_40, exp_M_40, C_v_40, X_40 = np.loadtxt(startPath + "L40" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_60, exp_M_60, C_v_60, X_60 = np.loadtxt(startPath + "L60" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_80, exp_M_80, C_v_80, X_80 = np.loadtxt(startPath + "L80" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)
exp_E_100, exp_M_100, C_v_100, X_100 = np.loadtxt(startPath + "L100" + endPath, dtype="double", usecols = (1,2,3,4), unpack = True, skiprows = 0)

#Text files with time step = 0.005
T_good, exp_E_40_good, exp_M_40_good, C_v_40_good, X_40_good = np.loadtxt(startPath + "parallel_L40_unordered_problem8.txt", dtype="double", usecols = (0,1,2,3,4), unpack = True)
T_narrow, exp_E_60_narrow, exp_M_60_narrow, C_v_60_narrow, X_60_narrow = np.loadtxt(startPath + "L60" + endPath2, dtype="double", usecols = (0,1,2,3,4), unpack = True)
exp_E_80_narrow, exp_M_80_narrow, C_v_80_narrow, X_80_narrow = np.loadtxt(startPath + "L80" + endPath2, dtype="double", usecols = (1,2,3,4), unpack = True)
exp_E_100_narrow, exp_M_100_narrow, C_v_100_narrow, X_100_narrow = np.loadtxt(startPath + "L100" + endPath2, dtype="double", usecols = (1,2,3,4), unpack = True)

##exp_E

plt.figure()
#plt.plot(T, exp_E_40, 'o-', label="L40", color="g")
plt.plot(T, exp_E_60, 'o-',label="L60", color="darkgreen")
plt.plot(T, exp_E_80, 'o-',label="L80", color="mediumblue")
plt.plot(T, exp_E_100, 'o-',label="L100", color="r")
plt.plot(T_good, exp_E_40_good, 'o',label="L40, step 0.005", color = 'indigo')
plt.plot(T_narrow, exp_E_60_narrow, 'o', label = "L60, step 0.005", color = 'forestgreen')
plt.plot(T_narrow, exp_E_80_narrow, 'o', label = "L80, step 0.005", color = 'dodgerblue')
plt.plot(T_narrow, exp_E_100_narrow, 'o', label = "L100, step 0.005", color = 'crimson')



plt.legend()
#plt.title("L=20 unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("$\epsilon$")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_exp_E.pdf")

##exp_M

plt.figure()
#plt.plot(T, exp_M_40, 'o-',label="L40", color="g")
plt.plot(T, exp_M_60, 'o-',label="L60", color="darkgreen")
plt.plot(T, exp_M_80, 'o-',label="L80", color="mediumblue")
plt.plot(T, exp_M_100, 'o-',label="L100", color="r")
plt.plot(T_good, exp_M_40_good, 'o',label="L40, step 0.005", color = 'indigo')
plt.plot(T_narrow, exp_M_60_narrow, 'o', label = "L60, step 0.005", color = 'forestgreen')
plt.plot(T_narrow, exp_M_80_narrow, 'o', label = "L80, step 0.005", color = 'dodgerblue')
plt.plot(T_narrow, exp_M_100_narrow, 'o', label = "L100, step 0.005", color = 'crimson')

plt.legend()
#plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("$m$")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_exp_M.pdf")

##C_v

plt.figure()
#plt.plot(T, C_v_40, 'o-',label="L40", color="g")
plt.plot(T, C_v_60, 'o-',label="L60", color="darkgreen")
plt.plot(T, C_v_80, 'o-',label="L80", color="mediumblue")
plt.plot(T, C_v_100, 'o-',label="L100", color="r")
plt.plot(T_good, C_v_40_good, 'o',label="L40, step 0.005", color = 'indigo')
plt.plot(T_narrow, C_v_60_narrow, 'o', label = "L60, step 0.005", color = 'forestgreen')
plt.plot(T_narrow, C_v_80_narrow, 'o', label = "L80, step 0.005", color = 'dodgerblue')
plt.plot(T_narrow, C_v_100_narrow, 'o', label = "L100, step 0.005", color = 'crimson')




plt.legend()
#plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("$C_v$")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_Cv.pdf")
plt.show()

##X

plt.figure()
plt.plot(T, X_60, 'o-',label="L60", color="darkgreen")
plt.plot(T, X_80, 'o-',label="L80", color="mediumblue")
plt.plot(T, X_100, 'o-',label="L100", color="r")
plt.plot(T_good, X_40_good, 'o',label="L40, step 0.005", color = 'indigo')
plt.plot(T_narrow, X_60_narrow, 'o', label = "L60, step 0.005", color = 'forestgreen')
plt.plot(T_narrow, X_80_narrow, 'o', label = "L80, step 0.005", color = 'dodgerblue')
plt.plot(T_narrow, X_100_narrow, 'o', label = "L100, step 0.005", color = 'crimson')


plt.legend()
#plt.title("Spins unordered")
plt.xlabel("T [J/$k_b$] ")
plt.ylabel("$\chi$")
# plt.xscale("log")
plt.grid(linestyle = '--', linewidth = 0.2)
plt.savefig("../out/plot8/8_X.pdf")
plt.show()
