import matplotlib.pyplot as plt

x = [1,2,3]
y1 = [2,3,4]
y2 = [4,3,2]

plt.plot(x, y1, label="Brasil")
plt.plot(x, y2, label="Inimigo")

plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()

plt.show()