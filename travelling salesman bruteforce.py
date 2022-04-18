from itertools import permutations
l=[1,2,3,4]
d={1:{2:10,3:15,4:20},2:{1:10,3:35,4:25},3:{1:15,2:35,4:30},4:{1:20,2:25,3:30}}
x=int(input("Enter the starting node"))
p=permutations([1,2,3,4],4)
p=list(p)
q=[]
s=0
f=[]
min=9999999
for i in p:
    s=0
    if(i[0]==x):
        for j in range(len(i)):
            s+=d[i[j%len(i)]][i[(j+1)%len(i)]]
        print(i,s)    
        if(s<min):
            f=i
            min=s
print("Success : ",f,min)        