def printpairs(arr,n):
    a=" "
    k=[]
    for i in range(n):
        for j in range(n):
            k.append(arr[i]+","+arr[j])
    g=[]
    for f in k:
        m,n=f.split(",")
        if(2*len(m)==len(n)):
            g.append(f)
    t=[]  
    for u in g:
        o,p=u.split(",")
        
        for l in o:
            if l in p :
                t.append(l)
    t.sort()
    if(len(t)>0):
        print(*t,sep=",")
    else:
        print("-1")
    
arr=list(map(str,input().split(",")))
printpairs(arr,len(arr))