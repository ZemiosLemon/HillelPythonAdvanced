class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        result = Point(
            self.x + other.x,
            self.y + other.y
        )
        return result



    def __sub__(self, other):
        result = Point(
            self.x - other.y,
            self.x - self.y
        )
        return result


    def __str__(self):
        return str(self.x)+' '+str(self.y)


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)


    def s_triangle(self):
        return 0.5*abs((self.b.x-self.a.x)*(self.c.y-self.a.y)-(self.c.x-self.a.x)*(self.b.y-self.a.y))

# 1/2*abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))

    def p_triangle(self):
        ab = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        bc = ((self.c.x - self.b.x) ** 2 + (self.c.y - self.b.y) ** 2) ** 0.5
        ac = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5
        result  = ab + bc + ac
        return result


    def change_coordinates(self, a1, b1, a2, b2, c1, c2):
        self.a.x = a1
        self.a.y = b1
        self.b.x = a2
        self.b.y = b2
        self.c.x = c1
        self.c.y = c2

triangele = Triangle(5, 4, -1, 2, -7, 3)
print(triangele.s_triangle())
print(triangele.p_triangle())
triangele.change_coordinates(4, 3, 0, 1, -6, 2)
print(triangele.p_triangle())
print(triangele.s_triangle())
