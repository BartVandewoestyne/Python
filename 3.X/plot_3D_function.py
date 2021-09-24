# Based on:
#   https://matplotlib.org/stable/gallery/mplot3d/surface3d.html
#   https://stackoverflow.com/questions/51891538/create-a-surface-plot-of-xyz-altitude-data-in-python

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Read CSV
csvFileName = sys.argv[1]
csvData = []
with open(csvFileName, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=' ')
    for csvRow in csvReader:
        csvData.append(csvRow)

# GetX, Y, Z
csvData = np.array(csvData)
csvData = csvData.astype(np.float)
X, Y, Z, A, B, C = csvData[:,0], csvData[:,1], csvData[:,2], csvData[:,3], csvData[:,4], csvData[:,5]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

Xpoly = np.arange(0, X[-1], 10)
Ypoly = np.arange(0, Y[-1], 10)
Xpoly, Ypoly = np.meshgrid(Xpoly, Ypoly)
Zpoly = np.polynomial.polynomial.polyval2d(Xpoly, Ypoly, [ [0, 0, 1], [0, 0, 0], [1, 0, 0] ])

surf = ax.plot_surface(Xpoly, Ypoly, Zpoly, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.scatter(X, Y, Z, c='red')

plt.show()
