try:
    t = int(input())
    while t:
        arr = list(map(int, input().split()))
        k = int(input())
        i = 9
        while k - arr[i] >= 0:
            k = k - arr[i]
            arr[i] = 0
            i -= 1
        print(i+1)
        t -= 1
except EOFError:
    pass