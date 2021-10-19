colors = ['red', 'green', 'green', 'red' , 'red']

measurements = ['green'] # test 1
motions = [[1]] # test 1
measurements = ['green', 'green', 'green' ,'green', 'green','red']  # test 2
motions = [[1],[0],[-1],[1],[1],[0]] # test 2

sensor_right = {}
sensor_right['green'] = 0.6
sensor_right['red'] = 0.8

p_move = 0.8

def compute_right(p):
    p_aux = []
    for i in range(len(p)):
        if i == 0:
            p_aux.append(p_move * p[len(p) - 1] + (1-p_move) * p[i])
        else:
            p_aux.append(p_move * p[i-1] + (1-p_move) * p[i])

    return p_aux

def compute_left(p):
    p_aux = []
    for i in range(len(p)):
        if i == (len(p) - 1):
            p_aux.append(p_move * p[0] + (1 - p_move) * p[i])
        else:
            p_aux.append(p_move * p[i + 1] + (1 - p_move) * p[i])

    return p_aux

def sense(p, Z):
    """Update belief array p according to new measurement Z"""
    # TODO: insert your code here

    for i in range(len(p)):
        if Z == colors[i]:
            p[i] = p[i] * sensor_right['green']
        else:
            p[i] = p[i] * (1.0 - sensor_right['red'])        

    norm = [float(i)/sum(p) for i in p]
    p = norm

    return p

def move(p, U):
    """Update p after movement U"""
    #TODO: insert your code here

    if U[0] == 1:
        p = compute_right(p)
    elif U[0] == -1:
        p = compute_left(p)

    return p

#main
if __name__ == '__main__':
    p = []

    width  = len(colors)
    n = width

    for c in range(width):
        p.append(1./n)


    for s in range(len(measurements)):
        print("sense ",measurements[s])
        p = sense(p,measurements[s])
        print(p)
        print("move ", motions[s])
        p = move(p,motions[s])
        print(p)


