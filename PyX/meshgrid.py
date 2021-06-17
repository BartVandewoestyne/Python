# Draw an XDS-RACU 33x33 meshgrid.
#
# Visualize with either one of
#
#   gv meshgrid.pdf (and scale to 'Fit to window')
#
#   xpdf meshgrid.pdf (and select 'Full screen')
#
# TODO:
#   - Investigate why the last lines are not drawn in the PNG.
#   - Draw rectangle representing (0,0-(maxX, maxY) in black.

from pyx import *
from xml.dom.minidom import *
from PIL import Image, ImageDraw

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


# TODO: warn if the XML is not valid (e.g. no range attribute)
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


def drawLine(line):

    # Bitmap coordinates follow same X/Y axes convention as our warpgrids.
    draw.line(line, fill=255)

    # Vector graphics coordinates have a different Y axes convention and
    # need to be flipped upside down.
    line[1] = height - line[1]
    line[3] = height - line[3] 
    c.stroke(path.line(*line), linestyle)


def saveWarpImages(warpfile):
    basename, extension = os.path.splitext(warpfile)
    c.writePDFfile(basename + ".pdf")
    c.writeEPSfile(basename + ".eps")
    c.writeSVGfile(basename + ".svg")
    im.save(basename + ".png", "PNG")
    

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
print(f'deltaX between grid points = {deltax} pixels')
print(f'deltaY between grid points = {deltay} pixels')

xcoords = [0]*nbpoints
ycoords = [0]*nbpoints

xcoordsFile = open("xcoords.txt", "w")
ycoordsFile = open("ycoords.txt", "w")

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
        ycoords[idx] = row*deltay + ydisplacement
        
        xcoordsFile.write("{:18} ".format(xcoords[idx]));
        ycoordsFile.write("{:18} ".format(ycoords[idx]));

    xcoordsFile.write("\n");
    ycoordsFile.write("\n");

xcoordsFile.close()
ycoordsFile.close()

# Prepare for vector-graphics drawing using PyX.
c = canvas.canvas()
linestyle = [style.linewidth(1.0), color.rgb.blue]
unit.set(defaultunit="pt")

# Prepare for bitmap drawing using PIL.
# Note that when drawing an image with resolution width x height, the
# coordinates of the pixels range from 0..width-1 and 0..height-1.
im = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(im)

# Draw 'horizontal' line segments.
for row in range(0, nrows):
    for col in range(0, ncols-1):
        idxStart = row*nrows + col
        idxEnd = idxStart + 1
        horLine = [xcoords[idxStart], ycoords[idxStart], xcoords[idxEnd], ycoords[idxEnd]]
        drawLine(horLine)

# Draw 'vertical' line segments.
for row in range(0,  nrows-1):
    for col in range(0, ncols):   
        idxStart = row*nrows + col
        idxEnd = (row+1)*nrows + col
        vertLine = [xcoords[idxStart], ycoords[idxStart], xcoords[idxEnd], ycoords[idxEnd]]
        drawLine(vertLine)

# Draw non-warped warp resolution rectangle.
shape = [(0, 0), (width, height)]
draw.rectangle(shape, outline ="black")
c.stroke(path.rect(0, 0, width, height))

saveWarpImages(warpfile)
