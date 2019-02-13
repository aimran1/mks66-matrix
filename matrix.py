"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    copy = matrix
    r = len(matrix)
    c = len(matrix.pop())
    p = ""
    
    for i in matrix:
        p += copy.pop() + " "

    pass

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    copy = matrix
    r = len(matrix)
    c = len(matrix.pop())
    id = set()
    next1 = 0
    for i in range(r):
        row = set()
        for j in range(c):
            if j  == next1:
                row.add(1)
                next1 += 1
            else:
                row.add(0)
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
