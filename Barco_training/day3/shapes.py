# TODO:
#   * Did I solve it as intended?
#   * How to implement get_type()?

import math

class Square(object):

    def __init__(self, sidelength):
        self.sidelength = sidelength

    def get_surface_area(self):
        return self.sidelength*self.sidelength

    def get_type(self):
        return "square"


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def get_surface_area(self):
        return self.radius*self.radius*math.pi

    # TODO: why may this be static???
    def get_type(self):
        return "circle"

def print_surface_area_of_object(object):
    if object.get_type() == "square":
        print("Surface area of square is {0}".format(object.get_surface_area()))
    elif object.get_type() == "circle":
        print("Surface area of circle is {0}".format(object.get_surface_area()))
    else:
        print("ERROR: cannot print surface area of this object.")

if __name__ == "__main__":

    c = Circle(2)
    s = Square(3)
    print_surface_area_of_object(c)
    print_surface_area_of_object(s)
