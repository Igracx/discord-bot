import numpy as np

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 10

screen_array2D = np.full((SCREEN_HEIGHT, SCREEN_WIDTH), 0)
#screen_array2D[4, 5] = 2
#screen_array2D[3, 5] = 2
#screen_array2D[5, 5] = 2
#screen_array2D[4, 6] = 2
#screen_array2D[4, 4] = 2

def convert_screen_array2D_to_string(screen_array_2D):
    screen_string = ''
    for array in screen_array_2D:
        for value in array:
            if value == 0:
                screen_string += 'X'
            elif value == 1:
                screen_string += 'O'
            elif value == 2:
                screen_string += ' '
        screen_string += '\n'
    return screen_string

def mark_pos(pos, screen_array2D):
    screen_array2D[pos[0], pos[1]] = 1
    screen_array2D[pos[0] + 1, pos[1]] = 2
    screen_array2D[pos[0] - 1, pos[1]] = 2
    screen_array2D[pos[0], pos[1] + 1] = 2
    screen_array2D[pos[0], pos[1] - 1] = 2

def msg():
    global screen_array2D
    #screen_array2D = np.full((SCREEN_WIDTH, SCREEN_HEIGHT), 0)
    #screen_array2D[4, 5] = 1
    #screen_array2D[3, 5] = 1
    #screen_array2D[5, 5] = 1
    #screen_array2D[4, 6] = 1
    #screen_array2D[4, 4] = 1
 
    return convert_screen_array2D_to_string(screen_array2D)

mark_pos((4, 5), screen_array2D)
mark_pos((8, 8), screen_array2D)
mark_pos((2, 2), screen_array2D)
print(msg())
