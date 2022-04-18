import numpy as np
from pyparsing import alphanums
import copy
from functools import cmp_to_key
from queue import PriorityQueue
uday_initial_state=[[2,0,3],[ 1,8,4],[7,6,5]]
uday_goal_state=[[1,2,3],[8,0,4],[7,6,5]]


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



def uday_manhatten(s,g):
    sum1=0
    for i in range(3):
        for j in range(3):
            if s[i][j]!=0:            
                for k in range(3):
                    for m in range(3):
                        if(s[i][j]==g[k][m]):
                            x2=k
                            y2=m
                sum1+=(abs(i-x2)+abs(j-y2))
    return sum1       
        

def uday_best_first_search(s,g):
    uday_closed=[]
    uday_pq=PriorityQueue()
    uday_pq.put((uday_manhatten(s,g),s))
    open=[]
    x=uday_pq.get()
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
                    # print(new)
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
                    # print(new)

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
                    # print(new)

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
                    # print(new)

                    # enqueue(new)


        # sorted(open,key=cmp_to_key(uday_manhatten)) 
        for i in open:
            uday_pq.put((uday_manhatten(i,g),i))       
        if (uday_pq.qsize()) > 0:
            alpha=uday_pq.get()
            # print(alpha)
            uday_curr_state = alpha[1]
            uday_closed.append(alpha[1])
        else:
            print ("not found")
            return


if __name__ == "__main__":
    uday_source = [[2,0,3],[ 1,8,4],[7,6,5]]
    uday_goal = [[1,2,3],[4,5,6],[8,7,0]]
    uday_best_first_search(uday_source,uday_goal)