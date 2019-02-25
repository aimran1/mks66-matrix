from display import *
from draw import *
from matrix import *

screen = new_screen()
white = [ 255, 255, 255 ]
red = [250,0,0]
blue = [0,0,255]
matrixr = new_matrix()
matrixw = new_matrix()
matrixb = new_matrix()

def add_square(matrix,x0,y0,z0,size):
    add_edge(matrix, x0, y0, z0, x0, y0+size, z0)
    add_edge(matrix, x0, y0, z0, x0+size, y0, z0)
    add_edge(matrix, x0, y0+size, z0, x0+size, y0+size, z0)
    add_edge(matrix, x0+size, y0+size, z0, x0+size, y0, z0)

def add_row(matrix,color,x0):
    while x0 + 10 < 500:
        add_square(matrix,x0,y0,0,38)
        x0 += 2

y0 = 0
for i in range(13):
    x0 = 0
    if y0 >= 228:
        while x0 < 162:
            if x0 % 20 == 0:
                add_square(matrixw,x0+12,y0+15,0,10)
            else:
                add_square(matrixb,x0,y0,0,38)
            x0+=1
        x0 = 200
    if i % 2 == 0:
        add_row(matrixr,red,x0)
    else:
        add_row(matrixw,white,x0)
    y0 += 38

draw_lines(matrixr,screen,red)
draw_lines(matrixb,screen,blue)
draw_lines(matrixw,screen,white)
display(screen)
