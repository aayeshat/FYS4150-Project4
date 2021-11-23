import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import linregress
import statistics as stat
import operator

mpl.rcParams["axes.titlesize"] = 16
mpl.rcParams["axes.labelsize"] = 14
mpl.rcParams["xtick.labelsize"] = 12
mpl.rcParams["ytick.labelsize"] = 12
mpl.rcParams["legend.fontsize"] = 7.5
plt.rcParams["figure.figsize"] = (7,5)

startPath = "../out/data_8/energy_";
endPath = "_unordered_limitedT.txt"

T = np.loadtxt(startPath + "L60" + endPath, dtype="double", usecols = (0), unpack = True, skiprows = 0)

T_40, C_v_40, X_40 = np.loadtxt("../out/data_8/energy_parallel_L40_unordered_problem8.txt", dtype="double", usecols = (0,3,4), unpack = True)
T_60, C_v_60, X_60 = np.loadtxt(startPath + "L60" + endPath, dtype="double", usecols = (0, 3,4), unpack = True, skiprows = 0)
T_80, C_v_80, X_80 = np.loadtxt(startPath + "L80" + endPath, dtype="double", usecols = (0, 3,4), unpack = True, skiprows = 0)
T_100, C_v_100, X_100 = np.loadtxt(startPath + "L100" + endPath, dtype="double", usecols = (0, 3,4), unpack = True, skiprows = 0)

Cv_5max_40 = (np.argsort(C_v_40)[-5:])
Cv_5max_60 = (np.argsort(C_v_60)[-5:])
Cv_5max_80 = (np.argsort(C_v_80)[-5:])
Cv_5max_100 = (np.argsort(C_v_100)[-5:])

print(Cv_5max_40)
print(Cv_5max_60)
print(Cv_5max_80)
print(Cv_5max_100)

#Using output
T_indices_40 = (39, 40, 41, 36, 37)
T_indices_60 = (9, 7, 8, 6, 4)
T_indices_80 = (7, 8, 4, 6, 5)
T_indices_100 = (4, 8, 7, 6, 5)

Tc_40 = [T_40[i] for i in T_indices_40]
Tc_60 = [T_80[i] for i in T_indices_60]
Tc_80 = [T_80[i] for i in T_indices_80]
Tc_100 = [T_100[i] for i in T_indices_100]

Tc_40 = stat.mean(Tc_40)
Tc_60 = stat.mean(Tc_60)
Tc_80 = stat.mean(Tc_80)
Tc_100 = stat.mean(Tc_100)
print(Tc_40, Tc_60, Tc_80, Tc_80)

Tc_values = [Tc_40, Tc_60, Tc_80, Tc_100]
Tc_values = [Tc_100, Tc_80, Tc_60, Tc_40]
print(Tc_values)


L_inv = [0.01, 0.0125, 1/60.0, 0.025]

x = np.arange(0.0, 0.025, 0.0001)
y = (1.0457142857143151 * x )+ 2.2667857142857137

L_new = [0.0125, 1/60.0, 0.025]
Tc_new = [Tc_80, Tc_60, Tc_40]
print(L_new, Tc_new)
lin_reg = linregress(L_new, Tc_new)
print(lin_reg)
#LinregressResult(slope=1.0457142857143151, intercept=2.2667857142857137, rvalue=0.9995971261503047, pvalue=0.018071501645655245, stderr=0.029692299558328507, intercept_stderr=0.0005578749768505673)

plt.figure()
#plt.plot(L_inv, Cv_max, 'o', label = "$C_v$ maxima, L = 40, 60, 80, 100")
plt.plot(x, y, label = "Slope of linear regression")
plt.plot(L_inv, Tc_values, 'o', label = "Tc for L = 100, 80, 60, 40")
plt.xlim(0.00,0.026)
plt.xlabel("1/L")
plt.ylabel("T [J/k$_b$]")
plt.legend()
plt.savefig("../out/plot8/crit_temp.pdf")
plt.show()
