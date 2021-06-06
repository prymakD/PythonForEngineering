import matplotlib.pyplot as plt

file = open('bars.txt', 'r')
X = [float(x) for x in ((file.readline()).split())]
Y = [float(x) for x in ((file.readline()).split())]

plt.bar(X, Y, align='edge',
        color=['peru', 'sienna', 'sandybrown', 'peru', 'saddlebrown', 'sienna', 'saddlebrown', 'sienna', 'saddlebrown',
               'black', 'black', 'black'])
#The bars are positioned at x with the given alignment.
# Their dimensions are given by height and width.
# The vertical baseline is bottom (default 0).

for x, y in zip(X, Y):
    plt.text(x, y, str(y)) #Add the text to the Axes at location x, y in data coordinates.

plt.xlim(0)
plt.show()
