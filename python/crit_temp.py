import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import linregress

# T, C_v_ordered_20 = np.loadtxt(basepath +"/energy_L20_ordered_problem8.txt", dtype="double", usecols = (0,3), unpack = True, skiprows = 0)
# T, C_v_ordered_40 = np.loadtxt(basepath +"/energy_L40_ordered_problem8.txt", dtype="double", usecols = (0,3), unpack = True, skiprows = 0)
# T, C_v_ordered_80 = np.loadtxt(basepath +"/energy_L80_ordered_problem8.txt", dtype="double", usecols = (0,3), unpack = True, skiprows = 0)
# T, C_v_ordered_100 = np.loadtxt(basepath +"/energy_L100_ordered_problem8.txt", dtype="double", usecols = (0,3), unpack = True, skiprows = 0)
#
Cv_max_20 = (np.sort(C_v_ordered_20)[-5:])/5.0
Cv_max_40 = (np.sort(C_v_ordered_40)[-5:])/5.0
Cv_max_80 = (np.sort(C_v_ordered_80)[-5:])/5.0
Cv_max_100 = (np.sort(C_v_ordered_100)[-5:])/5.0
#
# Cv_max = [Cv_max_20, Cv_max_40, Cv_max_80, Cv_max_100]
# L = [1/100.0, 1/80.0, 1/40.0, 1/20.0]

# lin_regress = linregress(L, Cv_max)

X = [2, 4, 6, 8]
Y = [2, 4, 7, 8]

sorted = np.sort(X)[-3:]


print(sorted)


lin_reg = linregress(X,Y)
print(lin_reg)

# plt.figure()
# plt.plot(L, Cv_max)
