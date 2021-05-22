import math
import numpy  as np

class Points ( object ) :
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z
        # print('in initializer',self.x,self.y,self.z)
    def __sub__(self, no) :
        return Points(*[self.x-no.x,self.y-no.y,self.z-no.z])
    def dot(self, no) :
        return self.x*no.x+self.y*no.y+self.z*no.z
    def cross(self, no) :
        c=[]
        c.append(self.y*no.z-self.z*no.y)
        c.append(self.z*no.x-self.x*no.z)
        c.append(self.x*no.y-self.y*no.x)
        return Points(*c)
    def absolute(self) :
        return pow ( (self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5 )


if __name__ == '__main__' :
    points=[[1,2,3],[2,3,4]]
    x= Points(*points[0])
    y= Points(*points[1])
    print(x.cross(y))
    x= np.array([1,2,3])
    y=np.array([2,3,4])
    print(np.cross(x,y))
    print ( np.dot ( x, y ) )

    # points = list ()
    # for i in range ( 4 ) :
    #     a = list ( map ( float, input ().split () ) )
    #     points.append ( a )
    #
    # a, b, c, d = Points ( *points[0] ), Points ( *points[1] ), Points ( *points[2] ), Points ( *points[3] )
    # x = (b - a).cross ( c - b )
    # y = (c - b).cross ( d - c )
    # angle = math.acos ( x.dot ( y ) / (x.absolute () * y.absolute ()) )
    #
    # print ( "%.2f" % math.degrees ( angle ) )