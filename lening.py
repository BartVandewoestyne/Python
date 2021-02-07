#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

with open("../data/kapitaal.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Lening")
ax1.set_xlabel('Date')
ax1.set_ylabel('Kapitaal')

ax1.plot(x, y, c='r', label='kapitaal')

leg = ax1.legend()

plt.show()
