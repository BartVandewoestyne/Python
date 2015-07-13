import math


class Square(object):

    def __init__(self, side_length):
        self.side_length = side_length

    def get_surface_area(self):
        return self.side_length*self.side_length

    def get_type(self):
        return "square with side length {0}".format(self.side_length)


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def get_surface_area(self):
        return self.radius*self.radius*math.pi

    def get_type(self):
        return "circle with radius {0}".format(self.radius)


def print_surface_area_of_object(obj):
    """
    Note that we can call get_type() and get_surface_area() on obj here without inheritance!
    """
    print("Surface area of {0} is {1}.".format(obj.get_type(), obj.get_surface_area()))

if __name__ == "__main__":

    c = Circle(2)
    s = Square(3)
    print_surface_area_of_object(c)
    print_surface_area_of_object(s)
