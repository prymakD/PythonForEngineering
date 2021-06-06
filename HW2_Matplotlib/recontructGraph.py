import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 7, 4.5, 8]

a = [1, 2, 3, 4]
b = [3.5, 4, 6, 6.5]

plt.plot(x, y, label='funkcja 1', linestyle="-.", marker="o", color="green")
plt.plot(a, b, label='funkcja 2', linestyle="dashed", marker="<", color="red")

plt.xlim(0.5, 4.5)
plt.xticks([1, 2, 3, 4])

plt.ylim(2.5, 8.6)
plt.yticks([3, 7, 4.5, 8])

plt.xlabel("Parametr X")
plt.ylabel("Parametr Y")
plt.title("Wykres - XY")

plt.legend()

plt.savefig('exercise1.png')
