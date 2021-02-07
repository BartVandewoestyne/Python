# Draw an XDS-RACU 33x33 meshgrid.
#
# Visualize with either one of
#
#   gv meshgrid.pdf (and scale to 'Fit to window')
#
#   xpdf meshgrid.pdf (and select 'Full screen')
#
# TODO:
#   * Allow X and Y displacements.
#   * Load meshgrid from XML-file.

from pyx import *

unit.set(defaultunit="pt")

nrows = 33
ncols = 33
width = 2560
height = 1600

deltax = width/(ncols-1)
deltay = height/(nrows-1)

c = canvas.canvas()

linestyle = [style.linewidth.THICK, color.rgb.blue]

for row in range(0,nrows):
    c.stroke(path.line(0, row*deltay, width, row*deltay), linestyle)
for col in range(0,ncols):
    c.stroke(path.line(col*deltax, 0, col*deltax, height), linestyle)

c.writePDFfile("meshgrid")
