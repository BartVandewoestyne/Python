# Draw an XDS-RACU 33x33 meshgrid.
#
# Visualize with either one of
#
#   gv meshgrid.pdf (and scale to 'Fit to window')
#
#   xpdf meshgrid.pdf (and select 'Full screen')

from pyx import *
from xml.dom.minidom import *
import math
import os
import random
import sys

# Source:
#   https://stackoverflow.com/questions/15390807/integer-square-root-in-python
# Note that since Python 3.8, there is math.isqrt()
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def readWarp(warpfile):
    dom = parse(warpfile)    
    XFlatParametersElement = dom.getElementsByTagName("X-FlatParameters")[0]
    YFlatParametersElement = dom.getElementsByTagName("Y-FlatParameters")[0]
    xFlatsString = XFlatParametersElement.firstChild.nodeValue
    yFlatsString = YFlatParametersElement.firstChild.nodeValue
    warp = dict()
    warp['xrange'] = int(XFlatParametersElement.getAttribute("range"))
    warp['yrange'] = int(YFlatParametersElement.getAttribute("range"))
    warp['xFlats'] = [float(xFlatValue) for xFlatValue in xFlatsString.split()]
    warp['yFlats'] = [float(yFlatValue) for yFlatValue in yFlatsString.split()]
    return warp
    

unit.set(defaultunit="pt")

warpfile = sys.argv[1]
warp = readWarp(warpfile)

nrows = isqrt(len(warp['xFlats']))
ncols = isqrt(len(warp['yFlats']))
nbpoints = nrows*ncols
assert nrows*nrows == len(warp['xFlats'])
assert ncols*ncols == len(warp['yFlats'])

print(f'Found a {nrows} x {ncols} grid ({nbpoints} grid points in total).')

width = warp['xrange']
height = warp['yrange']
deltax = width/(ncols-1)
deltay = height/(nrows-1)

xcoords = [0]*nbpoints
ycoords = [0]*nbpoints

for row in range(0, nrows):
    for col in range(0, ncols):
        idx = row*nrows + col
        factor = 0.5  # determines how much deformation of the grid we have.
        
        # Random X and Y displacements.
        #xdisplacement = factor*random.uniform(-deltax/2, deltax/2)
        #ydisplacement = factor*random.uniform(-deltay/2, deltay/2)

        # X and Y displacements from warp file
        xdisplacement = warp['xFlats'][idx]
        ydisplacement = warp['yFlats'][idx]
        
        xcoords[idx] = col*deltax + xdisplacement
        ycoords[idx] = height - (row*deltay + ydisplacement)  # Y-coordinates are upside-down.

c = canvas.canvas()

linestyle = [style.linewidth(1.0), color.rgb.blue]

# Draw 'horizontal' line segments.
for row in range(0, nrows):
    for col in range(0, ncols-1):
        idxStart = row*nrows + col
        idxEnd = idxStart + 1
        c.stroke(path.line(xcoords[idxStart], ycoords[idxStart], xcoords[idxEnd], ycoords[idxEnd]), linestyle)

# Draw 'vertical' line segments.
for row in range(0,  nrows-1):
    for col in range(0, ncols):   
        idxStart = row*nrows + col
        idxEnd = (row+1)*nrows + col
        c.stroke(path.line(xcoords[idxStart], ycoords[idxStart], xcoords[idxEnd], ycoords[idxEnd]), linestyle)

basename, extension = os.path.splitext(warpfile)
c.writePDFfile(basename + ".pdf")
