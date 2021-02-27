try:
    t = int(input())
    while t:
        n, k = map(int, input().split())
        if k != 0:
            result = n % k
            print(result)
        else:
            print(n) 
        t -= 1
except EOFError:
    pass
