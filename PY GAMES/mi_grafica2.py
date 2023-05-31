import matplotlib.pyplot as plt

x = [2,3,4,5,6,7,8,9,10]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')
plt.show()