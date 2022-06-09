def diamond(A,n,k):
    array=[]
    for i in range(n):
        array.append(A[i])
    array.sort()
    ans=0
    while(len(array)>0 and k>0):
        array.sort()
        top=array[len(array)-1]
        array=array[0:len(array)-1]
        ans+=top
        top=top//2
        array.append(top)
        k-=1
    print(ans)
if __name__=='__main__':
    A=[2,1,7,4,2]
    k=3
    n=len(A)
diamond(A,n,k)  

    
