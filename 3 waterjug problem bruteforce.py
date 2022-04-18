from itertools import combinations, permutations
from random import randint

check = False

def fill(s,idx):
    capacity=[12,8,5]
    if(s[idx]<capacity[idx]):
        check=True
        s[idx]=capacity[idx]#fill first
    return s,check    
def empty(s,idx):
    capacity=[12,8,5]
    if(s[idx]>0):
        check=True
        s[idx]=0#fill first   
    return s,check
def transfer(s,t,f):
    check=True
    capacity=[12,8,5]
    x=min(s[f],abs(capacity[t]-s[t]))
    if(x==0):
        check=False
    s[f]-=x
    s[t]+=x
    return s,check
def solve(s,g):
    capacity=[12,8,5]
    to=0
    _from=1
    y=-1
    yin=-1
    c=permutations([0,1,2],2)
    c=list(c)
    counter=0
    c1=0
    print(s)
    while(1):
        counter+=1
        comb=c[counter%6]
        to,_from=comb
        if(s==g):
            print('suceess, goal achieved',c1)
            break
        y=randint(1,4)
        if(y!=yin):
            if(y==1 and s[to]==0):
                s,check=fill(s,to)
                if(check):
                    print(s)
                    c1+=1
            if(y==2 and s[to]==capacity[to]):
                s,check=empty(s,to)
                if(check):
                    print(s)
                    c1+=1
            if(y==3):
                s,check=transfer(s,to,_from)
                if(check):
                    print(s)
                    c1+=1
            if(y==4):
                s,check=transfer(s,_from,to)
                if(check):
                    print(s)
                    c1+=1
        yin=y
        
        
            




if __name__=="__main__":
    s=[12,0,0]
    g=[6,0,0]
    solve(s,g)  