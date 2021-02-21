try:    
    t = int(input())
    while t:
        x, y, n = map(int, input().split())
        temp = (n - y) // x
        print(temp*x + y)
        t -= 1
except EOFError:
    pass
