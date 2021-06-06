import matplotlib.pyplot as plt

x = [0, 1, 2, 3,4]
y = [0, 2.2,2.5, 2.7,3]


plt.plot(x,y, linestyle= "-.", marker="o" , color = "red", markerfacecolor='blue')

plt.grid(b=True, which='major',linestyle='-')

plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='-', alpha=0.1)
plt.xlim(left=0,right=4)
plt.ylim(top=3,bottom=0)

frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])
plt.show()