colors = ['red', 'green', 'green', 'red' , 'red']

motions = [[1]]                      # test 1
motions = [[1],[0],[-1],[1],[0]]     # test 2
# test 2 solution: .148 .42 .352 .064 .016

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
    p = [0.5, 0.5, 0, 0, 0]

    width  = len(colors)
    n = width

    for s in range(len(motions)):
        p = move(p,motions[s])

    print(p)

