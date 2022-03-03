def FN(num) :
    val=0
    if len(fn_ls)-1>=num :
        return fn_ls[num]
    else :
        val=sum(fn_ls[-2:])
        fn_ls.append(val)
        FN(num)

n=int(input())
fn_ls=[0,1]

print(fn_ls)
print(FN(n))

    