def result(a,b):
    return a*b + a -b

try:
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        max1 = max(arr)
        arr.remove(max1)
        max2 = max(arr)
        min1 = None
        min2 = None
        if arr:
            min1 = min(arr)
            arr.remove(min1)
        if arr:
            min2 = min(arr)
        if not min1 or not min2:
            a,b = max1,max2
        elif max1*max2 < min1* min2:
            a,b = min1,min2
        else:
            a,b = max1,max2
        
        print(result(a,b))
        t -= 1
except EOFError:
    pass
