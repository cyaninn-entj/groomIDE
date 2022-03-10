def FN(num) :
    i=num
    if len(fn_ls)-1>=num :
        return fn_ls[num]
    else :
        fn_ls.append(fn_ls[-1]+fn_ls[-2])
        return FN(i)

n=int(input())
fn_ls=[0,1]

print(FN(n))
#print(fn_ls)

    