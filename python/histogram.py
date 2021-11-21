from matplotlib import pyplot as plt
import numpy as np

samples_T1_ord = np.loadtxt("../out/data/samples_T1.0_ordered_problem6.txt")
samples_T1_unord = np.loadtxt("../out/data/samples_T1.0_unordered_problem6.txt")

samples_T24_unord = np.loadtxt("../out/data/samples_T2.4_unordered_problem6.txt")
samples_T24_ord = np.loadtxt("../out/data/samples_T2.4_ordered_problem6.txt")

# n_bins = 180
n_bins = 120
# bin_width = (x_plot_max - x_plot_min) / float(n_bins)

# plt.xlim(-2.01,-1.8)
# plt.hist(samples_T1_ord, density = True)
# plt.hist(samples_T1_unord, density = True)
# plt.hist(samples_T24_ord, density = True)
plt.hist(samples_T24_unord, density = True)
plt.show()
# plt.savefig("../out/plot/histogram_high_T.pdf")
