from matplotlib import pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

X = np.linspace(-np.pi, np.pi, 500)
C = np.cos(X)
S = np.sin(X)

plt.plot(X, C, color="blue", linewidth=1, label="cos")
plt.plot(X, S, color="red", linewidth=2, label="sin")
# plt.plot(X[::50], C[::50], linewidth=0, marker="o", color="green", markersize=10)

plt.xlim(1.1*X.min(), 1.1*X.max())
plt.ylim(1.1*C.min(), 1.1*C.max())

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           ["-pi", "-pi/2", "0", "pi/2", "pi"])
plt.yticks([-1, 0, 1])

ax = plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

ax.spines["left"].set_position(("data", 0))
ax.spines["bottom"].set_position(("data", 0))

plt.grid(which="minor")
plt.grid(which="major")
# plt.grid(which="both") same as in the top lines
plt.minorticks_on()

plt.legend(loc="best")
plt.show()