try:
    t = int(input())
    while t:
        n = int(input())
        while n % 2 == 0:
            n = n // 2
        if n == 0 or n == 1:
            print('NO')
        else: 
            print('YES')
        t -= 1
except EOFError:
    pass
