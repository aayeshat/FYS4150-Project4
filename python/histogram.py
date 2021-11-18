from matplotlib import pyplot as plt
import numpy as np

samples_T1_ord = np.loadtxt("../out/data/energy_T1.0_ordered_problem5.txt")
samples_T1_unord = np.loadtxt("../out/data/energy_T1.0_unordered_problem5.txt")
samples_T24_unord = np.loadtxt("../out/data/energy_T2.4_unordered_problem5.txt")
samples_T24_ord = np.loadtxt("../out/data/energy_T2.4_ordered_problem5.txt")

n_bins = 100
x_plot_min = 0.0
x_plot_max = 50.0
bin_width = (x_plot_max - x_plot_min) / float(n_bins)

lowT_ord = np.histogram(samples_T1_ord, bins = n_bins, density = 1, range = (x_plot_min, x_plot_max))
lowT_unord = np.histogram(samples_T1_unord, bins = n_bins, density = 1)

highT_ord = np.histogram(samples_T24_ord, bins = n_bins, density = 1)
highT_unord = np.histogram(samples_T24_unord, bins = n_bins, density = 1)

plt.hist(lowT_ord)
# plt.hist(lowT_unord)
# plt.hist(highT_ord)
# plt.hist(highT_unord)
plt.show()
plt.savefig("../out/plot/histogram_lowT_ord.pdf")
