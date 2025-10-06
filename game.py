x=[1,4,2,6,8,7,5]
y=[]
for i in x:
    d=2
    while d<=i//2:
        if i%d==0:
            break
        d=d+1
    else:
        y.append(i)
print(y)
       
        

    
