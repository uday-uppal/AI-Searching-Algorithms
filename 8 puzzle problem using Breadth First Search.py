import numpy as np
open=[]
closed=[]
from pyparsing import alphanums


q=[]
initial_state=[[2,0,3],[ 1,8,4],[7,6,5]]
goal_state=[[1,2,3],[8,0,4],[7,6,5]]
def manhatten(s,g):
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
manhatten(initial_state,goal_state)
        
alpha=-1
def up(l1,i,j):
    l1[i,j]=alpha
    l1[i,j]=l1[i,j+1]
    l1[i,j+1]=alpha

def down(l1,i,j):
    l1[i,j]=alpha
    l1[i,j]=l1[i,j-1]
    l1[i,j-1]=alpha
def right(l1,i,j):
    l1[i,j]=alpha
    l1[i,j]=l1[i+1,j]
    l1[i+1,j]=alpha
def left(l1,i,j):
    l1[i,j]=alpha
    l1[i,j]=l1[i-1,j]
    l1[i-1,j]=alpha
    
def same(s,g):
    alpha=True
    for i,k in s,g:
        for j,m in i,k:
           if(j!=m):
               alpha=False 
    return alpha
def movegen(l1,i,j):
    if(i<3):
        right(l1,i,j)
print(same(initial_state,goal_state))

