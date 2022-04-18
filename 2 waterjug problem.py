from random import randint
check = False
def fill(s,idx):
    capacity=[4,3]
    if(s[idx]<capacity[idx]):
        check=True
        s[idx]=capacity[idx]#fill first
    return s,check    
def empty(s,idx):
    capacity=[4,3]
    if(s[idx]>0):
        check=True
        s[idx]=0#fill first   
    return s,check
def transfer(s,t,f):
    check=True
    capacity=[4,3]
    x=min(s[f],abs(capacity[t]-s[t]))
    if(x==0):
        check=False
    s[f]-=x
    s[t]+=x
    return s,check
def solve(s,g):
    capacity=[4,3]

    to=0
    _from=1
    y=-1
    print(s)
    while(1):
        if(s==g):
            print('suceess, goal achieved')
            break
        yin=y
        y=randint(1,4)
        if(y!=yin):
            if(y==1 and s[to]==0):
                s,check=fill(s,to)
                if(check):
                    print(s)
                    check=False
            if(y==2 and s[to]==capacity[to]):
                s,check=empty(s,to)
                if(check):
                    print(s)
                    check=False                
            if(y==3):
                s,check=transfer(s,to,_from)
                if(check):
                    print(s)
                    check=False                
            if(y==4):
                s,check=transfer(s,_from,to)
                if(check):
                    print(s)
                    check=False        
            to,_from=_from,to




if __name__=="__main__":
    s=[0,0]
    g=[2,0]
    solve(s,g)
