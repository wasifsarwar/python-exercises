###
### Author: Sornali Rahman
### Class: CSc 110
### Description: This program displays a landscape in which a
###              'vanishing point' may be seen while dragging the
###              landscape up and down.
###

from graphics import graphics

def draw_sky_and_land(gui):
    '''
    Draws the sky and the grass.
    gui should be a graphics object.
    '''
    gui.rectangle(0, 0, 600, 600, 'sky blue')

    gui.ellipse(400, 90, 90, 90, 'yellow')

    #cloud1
    gui.ellipse(70, 70, 110, 60, 'white')
    gui.ellipse(50, 90, 110, 60, 'white')

    #cloud2
    gui.ellipse(285, 80, 140, 80, 'white')
    gui.ellipse(310, 50, 110, 60, 'white')

    #cloud 3
    gui.ellipse(445, 160, 140, 80, 'white')
    gui.ellipse(470, 140, 110, 60, 'white')



def draw_mountain(gui):
    '''
    This function should draw a mountain.
    gui should be a graphics object.
    '''
    y = gui.mouse_y / 3

    shape_y1 = 0 + y


    # Use this to shift the mountain as it shrinks/grows

    gui.triangle(250, shape_y1, 0, 500, 500, 500, 'brown')

    #this draws the horizon
    gui.rectangle(0, 350, 500, 500, 'green')

def draw_grass(gui):
    '''
    This function draws the blades of grass
    gui should be a graphics object
    '''
    i = 0
    while i < 500:
        offset = i * 15
        if i % 2 == 0:
            gui.line(offset, 350, offset, 250, 'dark green', 25)
        i += 1


def draw_trees_and_pond(gui):

    y = gui.mouse_y /3
    shift = gui.mouse_y / 2

    #this draws the trees and allows the shift
    gui.rectangle(100,380, 30, 70, 'brown')
    gui.rectangle(370,380, 30, 70, 'brown')
    gui.ellipse(115,350,80,110,'dark green')
    gui.ellipse(385,350,80,110,'dark green')

    #this draws the pond and allows the shift
    gui.ellipse(250,390,180-y,20,'blue')


def main():
    gui = graphics(500, 500, 'vanishing point')
    while True:
        gui.clear()
        draw_sky_and_land(gui)
        draw_mountain(gui)
        draw_grass(gui)
        draw_trees_and_pond(gui)
        gui.update_frame(60)

main()