from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 14
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["legend.fontsize"] = 12
plt.rcParams["figure.figsize"] = (7,5)

samples_T1_ord = np.loadtxt("../out/data/samples_T1.0_ordered_problem6.txt")
samples_T1_unord = np.loadtxt("../out/data/samples_T1.0_unordered_problem6.txt")

samples_T24_unord = np.loadtxt("../out/data/samples_T2.4_unordered_problem6.txt")
samples_T24_ord = np.loadtxt("../out/data/samples_T2.4_ordered_problem6.txt")


plt.xlabel("$\epsilon$ [J]")
plt.ylabel("Probability, %")

# plt.xlim(-2.01,-1.95)
# plt.hist(samples_T1_ord, bins = 20, density = True, color = "lightskyblue", edgecolor = "crimson")
# #plt.hist(samples_T1_unord, bins = 100, density = True)
# plt.savefig("../out/plot/histogram_ord_lowT.pdf")
# plt.show()
#
#
# plt.hist(samples_T24_ord, bins = 115, density = True, color = "pink", edgecolor = "crimson")
# #plt.hist(samples_T24_unord, bins = 128, density = True, color = "pink", edgecolor = "red")
# plt.xlim(-1.9, -0.7)
# plt.savefig("../out/plot/histogram_ord_highT.pdf")
# plt.show()

plt.xlim(-2.05,-0.6)
plt.hist(samples_T1_ord, bins = 5, density = True, color = "lightskyblue", edgecolor = "crimson", label = "T = 1 J/k$_b$")
plt.hist(samples_T24_ord, bins = 115, density = True, color = "pink", edgecolor = "crimson", label = "T = 2.4 J/k$_b$")
plt.yscale("log")
plt.legend()
plt.savefig("../out/plot/histograms_ordered.pdf")
plt.show()
