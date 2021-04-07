from graphics import graphics
import campus

def get_locations():
    '''
    This function's job is to load in the path file.
    The function will prompt the user for a file name, and then loac those
    contents into a a 2D list.
    Each row of the list represents one of the locations along the path.
    Each inner list will have three elements - the x coordinate, the y
    coordinate and lastly the name of the location.
    '''
    path = input('Path file name: ')
    path_file = open(path, 'r')
    locations = []
    for line in path_file:
        sp = line.split(' - ')
        loc = sp[1].split(',')
        locations.append([int(loc[0]), int(loc[1]), sp[0]])
    print(locations)
    return locations

def main():

    gui = graphics(1000, 560, "the path finder")
    pi = gui.image(0, 0, 1, 1, "campus.gif")
    gui.update_frame(100)
    locations = get_locations()
    gui.ellipse(locations[0][0], locations[0][1], 12, 12, '#003399')
    gui.text(locations[0][0], locations[0][1], locations[0][2], '#003399', 20)



    #loading the campus 2d grid
    campus_grid = campus.campus_grid

def draw(campus_grid, locations):



main()