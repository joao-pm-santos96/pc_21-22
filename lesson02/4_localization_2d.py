from typing import cast


colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green']                                        # test 1
motions = [[1,0]]                                               # test 1
measurements = ['green', 'red', 'red' ,'green', 'red','red']    # test 2
motions = [[1,0],[0,0],[0,1],[0,1],[-1,0],[0,0]]                # test 2

sensor_right = {}
sensor_right['green'] = 0.8
sensor_right['red'] = 0.7

p_move = 1.0

def show(p):
    for i in range(len(p)):
        print(p[i])

def compute_sense(p_ij, cell_color, Z):

    # get the probability of measuring 'color' knowing the robot is o 'x'
    p_color_x = 0
   
    if Z == 'green':
        if Z == cell_color:
            p_color_x = sensor_right['green']
        else:
            p_color_x = 1 - sensor_right['red']
    elif Z == 'red':

        if Z == cell_color:
            p_color_x = sensor_right['red']
        else:
            p_color_x = 1 - sensor_right['green']

    return(p_color_x * p_ij)

def sense(p, Z):
    """Update belief array p according to new measurement Z"""
    # TODO: insert your code here

    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] = compute_sense(p[i][j], colors[i][j], Z)

    # normalize
    all_sum = sum([sum(i) for i in p])
    p = [[j / all_sum for j in i] for i in p] 

    return p

def compute_move(p, pos, U):

    # get prior index
    prev_pos = [pos[0] - U[0], pos[1] - U[1]] 

    if prev_pos[0] < 0:
        prev_pos[0] = len(p) - 1
    elif prev_pos[0] > len(p) - 1:
        prev_pos[0] = 0

    if prev_pos[1] < 0:
        prev_pos[1] = len(p[0]) - 1
    elif prev_pos[1] > len(p[0]) - 1:
        prev_pos[1] = 0

    curr_prob = p[pos[0]][pos[1]]
    prev_prob = p[prev_pos[0]][prev_pos[1]]

    return p_move * prev_prob + (1 - p_move) * curr_prob    

def move(p, U):
    """Update p after movement U"""
    #TODO: insert your code here

    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] = compute_move(p, [i, j], U)

    return p

#main
if __name__ == '__main__': 
    height = len(colors)
    width  = len(colors[0])

    n = height * width

    p = []
    for l in range(height):
        q=[]
        for c in range(width):
            q.append(1./n)
        p.append(q)

    for s in range(len(measurements)):
        print("sense ",measurements[s])
        p = sense(p,measurements[s])
        show(p)
        print("move ", motions[s])
        p = move(p,motions[s])
        show(p)


