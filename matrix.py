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
    print(matrix)
    for i in matrix:
        print(i)
        for j in i:
            p += str(j) + " "
        p += "\n"
    print(p)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    r = len(matrix)
    c = len(matrix.pop())
    id = []
    next1 = 0
    for i in range(r):
        id.append([])
        for j in range(c):
            if j == next1:
                id[i].append(1)
            else:
                id[i].append(0)
        next1 += 1
    return(id)

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
