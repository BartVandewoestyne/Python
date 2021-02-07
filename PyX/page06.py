from math import pi
from pyx import *

c = canvas.canvas()

pt1 = path.circle(0, 0, 1).at(arclen=pi)
pt2 = path.circle(0, 0, 1).at(arclen=3*pi/2)

c.stroke(path.path(path.moveto(*pt1), path.lineto(*pt2)))

c.writeEPSfile("page06")
