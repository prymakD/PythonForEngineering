import matplotlib.pyplot as plt
import numpy as np

x = np.load('x.npy')
y = np.load('y.npy')

print(x)

f1 = np.poly1d(np.polyfit(x,y,1))
f2 = np.poly1d(np.polyfit(x,y,2))
f10 = np.poly1d(np.polyfit(x,y,10))

newx = np.linspace(0, 1, 1000)
plt.plot(newx, f1(newx))
plt.plot(newx, f2(newx))
plt.plot(newx, f10(newx))
plt.plot(x, y, '.')
plt.show()
