import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
        
    def __sub__(self, no):
        res=Points(self.x-no.x,self.y-no.y,self.z-no.z)
        return res
        
    def dot(self, no):
        res=self.x*no.x+self.y*no.y+self.z*no.z
        return (res)
        
    def cross(self, no):
        a1=self.x
        a2=self.y
        a3=self.z
        b1=no.x
        b2=no.y
        b3=no.z
        res=Points((a2*b3-a3*b2),(a1*b3-a3*b1),(a1*b2-a2*b1))
        return res
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
