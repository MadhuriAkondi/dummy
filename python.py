



def denomination(n):
    l=[500,5,50]
    l.sort(reverse=True)
    f=[]
    for i in l:
        f.append(n//i)
        n=n%i
    if(n!=0):
        print("denomination not possible")
        print("git test")
    else:
        for i in range(0,len(f)):
            print(l[i] , ":" , f[i])
            print("cash")
        
n = int(input())
print("git hello")
denomination(n);
print("Hi")
print("Hello")
