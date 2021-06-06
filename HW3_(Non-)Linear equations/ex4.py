import matplotlib.pyplot as plt
import numpy as np

a = np.random.uniform(low=-1, high = 1, size= 1000).reshape(500,2)
x = a[:,1] #taking all rows (:) but keeping the second column (1)
y = a[:,0]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)

mask = np.array(t>0)
t_jet = t[mask]
r_jet = r[mask]

inverted_mask = np.invert(mask)
t_terrain = t[inverted_mask]
r_terrain = r[inverted_mask]

plt.figure()

plt.axes(polar = True)
plt.scatter(t_jet,r_jet, c = r_jet, cmap = plt.cm.jet)
plt.scatter(t_terrain, r_terrain, c = r_terrain, cmap = plt.cm.terrain)

plt.show()
