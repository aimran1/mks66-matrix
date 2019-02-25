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
    p = ""
    for i in matrix:
        for j in i:
            p += str(j) + " "
        p += "\n"
    print(p)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    r = len(matrix)
    next1 = 0
    for i in range(r):
        for j in range(r):
            if j == next1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
        next1 += 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
"""
a a a a   b b b b
a a a a   b b b b
a a a a   b b b b
a a a a   b b b b
rows a ---> columns b ---> rows b
"""
def matrix_mult( m1, m2 ):
    m2c = m2.copy()
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for a in range(len(m2)):
                m2[i][j] += m1[i][a] * m2c[a][j]
                print(m2[i][j])
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
