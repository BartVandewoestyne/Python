import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(0, 1000, 1000)
y0p5 = x**(0.5)
y1 = x**1
y2 = x**2

fig, axs = plot.subplots(1, 2)
fig.suptitle('Afvlakking spotten...')
x_lim = 100
y_lim = 100

axs[0].grid(True, which="both")
axs[0].plot(x, y0p5, label="x^0.5")
axs[0].plot(x, y1, label="x^1")
axs[0].plot(x, y2, label="x^2")
axs[0].legend(loc="upper left")
axs[0].set_ylim([0, y_lim])
axs[0].set_xlim([0, x_lim])
axs[0].set_title('Lineair')
axs[0].set_xlabel('X')
#axs[0].set_ylabel('Y')
axs[0].legend(loc="upper right")

axs[1].grid(True, which="both")
axs[1].semilogy(x, y0p5, label="x^0.5")
axs[1].semilogy(x, y1, label="x^1")
axs[1].semilogy(x, y2, label="x^2")
axs[1].legend(loc="upper left")
axs[1].set_ylim([0.1, y_lim])
axs[1].set_xlim([0, x_lim]) 
axs[1].set_title('Logaritmisch')
axs[1].set_xlabel('X')
#axs[1].set_ylabel('Y')
axs[1].legend(loc="lower right")

plot.show()