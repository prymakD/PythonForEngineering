import matplotlib.pyplot as plt

file = open('data2.dat.txt', 'r')
x = [float(x) for x in ((file.readlines()))]

plt.subplot(211) #Add an Axes to the current figure or retrieve an existing Axes.
plt.hist(x, cumulative=True)
# histogram is computed where each bin gives the
# counts in that bin plus all bins for smaller values.
# The last bin gives the total number of datapoints
plt.subplot(212)
plt.hist(x)
plt.show()
