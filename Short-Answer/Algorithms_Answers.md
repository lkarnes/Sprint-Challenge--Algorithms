#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(2)


b)
O(n*2)

c)
O(n)
## Exercise II


func(nstory)

mid = nstory //2 

if dropegg(mid) == 'breaks' and dropegg(mid-1)=='breaks':
    return func(mid)
elif dropegg(mid) == 'breaks' and dropegg(mid-1) =='doesnt':
    return mid-1
elif dropegg(mid) == 'doesnt' and dropegg(mid-1) =='breaks':
    return mid
else: 
return func(mid + mid//2)

O(n)