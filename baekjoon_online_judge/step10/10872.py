#https://www.acmicpc.net/problem/10872

def pac(num,i) :
    if i==0 :
        return 1
    elif i==1 :
        return num
    else : 
        result=num*(i-1)
        return pac(result, i-1)
 
n=int(input())
print(pac(n,n))