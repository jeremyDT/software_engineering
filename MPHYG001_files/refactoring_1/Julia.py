from numpy import *
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def inner_loop(x, grid, x_size, y_size):

    for y in range(x_size):
        zx=1.5*(x-y_size/2)/(0.5*1*y_size)
        zy=(y-x_size/2)/(0.5*x_size)
        i=255
        t=True
        while t==True:
            if zx*zx+zy*zy>=4:
                t=False
            if i<=1:
                t=False
            a=zx*zx-zy*zy-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
            i=i-1
        grid[y][x]=i

    return grid

def make_mandelbrot(x_size = 600, y_size = 800):

    grid = zeros([x_size,y_size])

    for x in range(y_size):

        grid = inner_loop(x, grid, x_size, y_size)

    plt.imshow(grid)
    plt.savefig('Julia_plot.png')
    plt.close()
    plt.show()

if __name__ == '__main__':

    parser = ArgumentParser(description="Generate mandelbrot plot with the following input parameters: x_size = size of x-axis, y_size = size of y-axis")

    parser.add_argument('--x_size', default = 600, type = int)
    parser.add_argument('--y_size', default = 800, type = int)

    arguments= parser.parse_args()

    make_mandelbrot(x_size = arguments.x_size, y_size = arguments.y_size)