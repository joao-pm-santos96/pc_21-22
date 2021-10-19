colors = ['red', 'green', 'green', 'red' , 'red']

motions = [[1]]                      # test 1
#motions = [[1],[0],[-1],[1],[0]]     # test 2

p_move = 0.8

def move(p, U):
    """Update p after movement U"""
    #TODO: insert your code here

    return p

#main
p = [0.5, 0.5, 0, 0, 0]

width  = len(colors)
n = width

for s in range(len(motions)):
    p = move(p,motions[s])

print p

