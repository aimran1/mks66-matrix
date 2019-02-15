from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
"""
1  2  3  4      11  12  13  14
5  6  7  8      15  16  17  18
9  10 11 12     19  20  21  22
13 14 15 16     23  24  25  26
"""
#A = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}}
#B = {{11,12,13,14},{15,16,17,18},{19,20,21,22},{23,24,25,26}}
matrix_mult(matrix,ident(matrix))
draw_lines( matrix, screen, color )
display(screen)

"""




"""
