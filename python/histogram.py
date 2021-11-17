from matplotlib import pyplot as plt
import numpy as np

samples_T1_ord = np.loadtxt("../out/data/energy_T1.0_ordered_problem5.txt")
samples_T1_unord = np.loadtxt("../out/data/energy_T1.0_unordered_problem5.txt")
samples_T24_unord = np.loadtxt("../out/data/energy_T2.4_unordered_problem5.txt")
samples_T24_ord = np.loadtxt("../out/data/energy_T2.4_ordered_problem5.txt")

n_bins = 20

lowT_ord = np.histogram(samples_T1_ord)
lowT_unord = np.histogram(samples_T1_unord)

highT_ord = np.histogram(samples_T24_ord, bins = n_bins)
highT_unord = np.histogram(samples_T24_unord)

plt.hist(lowT_unord)
plt.hist(lowT_unord)
plt.hist(highT_ord)
plt.hist(highT_unord)
plt.show()
plt.savefig("../out/plot/5_histogram.pdf")
