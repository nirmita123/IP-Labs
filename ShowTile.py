"""Suraj Prathik Kumar
   2016101"""
#ShowTile.py
""" Illustrates the recursive procedure Tile.
This procedure ``tiles'' a given triangle with
smaller triangles.
Your task is to complete the Squares procedure
to obtain the figure as shared in the assignment
"""
from SimpleGraphics import *
class Point(object):
    """
    Attributes:
        x: float, the x-coordinate of a point
        y: float, the y-coordinate of a point
    """
    def __init__(self,x,y):
        """ Creates a point.
        PreC: x and y are floats
        """
        self.x = x
        self.y = y
    
    def Mid(self,other):
        """ Returns a point that encodes the midpoint of the
        line segment that connects self and other.
        
        PreC: other is a point
        """
        return Point((self.x+other.x)/2.0,(self.y+other.y)/2.0)

def DrawTriangle(P1,P2,P3,c):
    """ Draws a triangle with vertices P1, P2, and P3 and fillcolor c
    
    PreC: P1, P2, and P3 are points and c is a rgb list.
    """
    a = [P1.x,P2.x,P3.x]
    b = [P1.y,P2.y,P3.y]
    DrawPoly(a,b,FillColor=c)
    
def Tile(P1,P2,P3,L):
    """ Draws an L-level tiling of the
    triangle whose vertices are defined by P1, P2, and P3
    
    PreCond: P1, P2, and P3 are points and L is a nonnegative int.
    """
    if L==0:
        DrawTriangle(P1,P2,P3,YELLOW)
    else:
        # Compute the midpoint coordinates.
        P12 = P1.Mid(P2)
        P23 = P2.Mid(P3)
        P31 = P3.Mid(P1)
        # Paint the inner triangle
        DrawTriangle(P1,P2,P3,MAGENTA)
        # Partition each of the corner triangles
        Tile(P1,P31,P12,L-1)
        Tile(P2,P12,P23,L-1)
        Tile(P3,P23,P31,L-1)

def Squares(a,b,S,L):
    """Implement this to obtain squares
    with smaller squares, recursively
    a and b are coordinates of center of square.
    S is a non-negative integer representing side length of square
    L is a non-negative integer that indicates the levels of recursion
    """
    
    if L==0: 
        DrawRect(a,b,S,S,FillColor=YELLOW,EdgeWidth=0)
    else:
        DrawRect(a,b,S/3,S/3,FillColor=RED,EdgeWidth=0)
        S=S/3
        L=L-1
        Squares(a-S,b-S,S,L)
        Squares(a,b-S,S,L)
        Squares(a+S,b-S,S,L)
        Squares(a-S,b+S,S,L)
        Squares(a,b+S,S,L)
        Squares(a+S,b+S,S,L)
        Squares(a-S,b,S,L)
        Squares(a+S,b,S,L)
        
if __name__ == '__main__' :

    #To display the output from Squares procedure
    MakeWindow(25,bgcolor=BLACK,labels=False)
    Squares(0,0,24.0,5)
    Title('Recursive Squares')
    ShowWindow()

