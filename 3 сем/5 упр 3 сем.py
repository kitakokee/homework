#5 упр

import numpy as np
def spiral(N,M):

    A = np.zeros((N,M))
    A[0][0]=1
    count = 2
    x, y = 0, 0
    d_x, d_y = 0, 1
    while count <=N*M:
        if 0 <= x + d_x<=N - 1 and 0<= y+ d_y <= M - 1 and A[x + d_x][y + d_y] == 0:

            A[x+d_x][y+d_y] = count            
            x += d_x
            y += d_y 
            count += 1

        else:
            if d_y == 1:
                d_y = 0
                d_x = 1

            elif d_x == 1:                
                d_x = 0
                d_y = -1
                
            elif d_y == -1:                
                d_y = 0
                d_x = -1
                
            elif d_x == -1:                
                d_x = 0
                d_y = 1
    
    return A
print(spiral(5,6))
         