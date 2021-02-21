try:   
    t = int(input())
    while t:
        gcd = 1
        l, b = map(int, input().split())
        temp = min(l, b)
        for i in range(1, temp+1):
            if l % i == 0  and b % i == 0:
                gcd = i
        result = (l // gcd) * (b // gcd)
        print(result)         
        t -= 1
except EOFError:
    pass