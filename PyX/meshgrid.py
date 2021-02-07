# Draw an XDS-RACU 33x33 meshgrid.
#
# Visualize with either one of
#
#   gv meshgrid.pdf (and scale to 'Fit to window')
#
#   xpdf meshgrid.pdf (and select 'Full screen')
#
# TODO:
#   * Load X and Y displacements and resolution from XML-file.

from pyx import *
import random

unit.set(defaultunit="pt")

nrows = 33
ncols = 33
width = 2560
height = 1600

deltax = width/(ncols-1)
deltay = height/(nrows-1)

nbpoints = nrows*ncols
xcoords = [0]*nbpoints
ycoords = [0]*nbpoints

for row in range(0, nrows):
    for col in range(0, ncols):
        idx = row*nrows + col
        factor = 0.5  # determines how much deformation of the grid we have.
        xdisplacement = factor*random.uniform(-deltax/2, deltax/2)
        ydisplacement = factor*random.uniform(-deltay/2, deltay/2)
        xcoords[idx] = col*deltax + xdisplacement
        ycoords[idx] = row*deltay + ydisplacement

c = canvas.canvas()

linestyle = [style.linewidth.THICK, color.rgb.blue]

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

c.writePDFfile("meshgrid")
