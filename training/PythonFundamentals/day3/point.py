import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({0},{0})".format(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

if __name__ == "__main__":

    p1 = Point(10, 10)
    print(p1)
    p2 = Point(0, 0)
    print(p1.distance(p2))
