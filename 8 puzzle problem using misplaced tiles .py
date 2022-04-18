import numpy as np
from pyparsing import alphanums
import copy
from functools import cmp_to_key
from queue import PriorityQueue
# uday_initial_state=[[2,0,3],[ 1,8,4],[7,6,5]]
# uday_goal_state=[[1,2,3],[8,0,4],[7,6,5]]


def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return([i,j])

def right(a,pos):
    i,j = pos
    
    if j < 2:
        t = copy.deepcopy(a)
        t[i][j] = t[i][j+1]   # 0th tile = right tile 8
        t[i][j+1] = 0         #8th tile = 0
        return (t)
    else:
        return (a)

def left(a,pos):
    
    i,j = pos
    
    if j > 0:
        t = copy.deepcopy(a)
        t[i][j] = t[i][j-1]
        t[i][j-1] = 0
        return (t)
    else:
        return (a)

def up(a,pos):
    
    i,j = pos
    
    if i > 0:
        t = copy.deepcopy(a)
        t[i][j] = t[i-1][j]
        t[i-1][j] = 0
        return (t)
    else:
        return (a)

def down(a,pos):
    
    i,j = pos
    
    if i < 2:
        t = copy.deepcopy(a)
        t[i][j] = t[i+1][j]
        t[i+1][j] = 0
        return (t)
    else:
        return (a)



def uday_heuristic_function_misplaces_tiles(uday_s,uday_g):
    uday_sum=0
    for i in range(3):
        for j in range(3):
            if(uday_s[i][j]!=uday_g[i][j]):
                uday_sum+=1
    return uday_sum
def best_first_search(s,g):
    uday_closed=[]
    pq=PriorityQueue()
    pq.put((uday_heuristic_function_misplaces_tiles(s,g),s))
    open=[]
    x=pq.get()
    # print(x)
    uday_curr_state = x[1]
    uday_closed.append(uday_curr_state)
    if s == g:
        return

    while(1):        
        
        pos = find_pos(uday_curr_state)
        new = down(uday_curr_state,pos)
        if new != uday_curr_state:
            if new == g:
                print("Goal State Reached!!")
                print ("The intermediate states are:")
                uday_closed= uday_closed + [g]
                for i in uday_closed:
                  for j in i:
                    print(j)
                  print(" ")
                return
            else:
                if new not in uday_closed:
                    open.append(new)
                    print(new)
                    # enqueue(new)

        new = up(uday_curr_state,pos)
        if new != uday_curr_state:
            if new == g:
                print("Goal State Reached!!")
                print ("The intermediate states are:")
                uday_closed= uday_closed + [g]
                for i in uday_closed:
                  for j in i:
                    print(j)
                  print(" ")
                return
            else:
                if new not in uday_closed:
                    open.append(new)
                    print(new)

                    # enqueue(new)

        
        new = left(uday_curr_state,pos)
        if new != uday_curr_state:
            if new == g:
                print("Goal State Reached!!")
                print ("The intermediate states are:")
                uday_closed= uday_closed + [g]
                for i in uday_closed:
                  for j in i:
                    print(j)
                  print(" ")
                return
            else:
                if new not in uday_closed:
                    open.append(new)
                    print(new)

                    # enqueue(new)

            
        new = right(uday_curr_state,pos)
        if new != uday_curr_state:
            if new == g:
                print("Goal State Reached!!")
                print ("The intermediate states are:")
                uday_closed= uday_closed + [g]
                for i in uday_closed:
                  for j in i:
                    print(j)
                  print(" ")
                return
            else:
                if new not in uday_closed:
                    open.append(new)
                    print(new)

                    # enqueue(new)


        # sorted(open,key=cmp_to_key(uday_heuristic_function_misplaces_tiles)) 
        for i in open:
            pq.put((uday_heuristic_function_misplaces_tiles(i,g),i))       
        if (pq.qsize()) > 0:
            alpha=pq.get()
            # print(alpha)
            uday_curr_state = alpha[1]
            uday_closed.append(alpha[1])
        else:
            print ("not found")
            return


if __name__ == "__main__":
    uday_source = [[1,2,3],[4,5,6],[8,7,0]]
    uday_goal = [[1,2,3],[4,5,6],[7,8,0]]
    best_first_search(uday_source,uday_goal)