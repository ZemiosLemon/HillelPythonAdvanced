class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, point):
        result = (self.x - point.x) ** 2 + (self.y - point.y)
        if result <= self.radius ** 2:
            return True
        else:
            return False

    def __contains__(self, item):
        return self.contains(item)


p = Point(4, -4)
c = Circle(2, 5, 3)
print(c.contains(p))
print(p in c)
