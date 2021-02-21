import math
try: 
    t = int(input())
    while t:
        a, b = map(int, input().split())
        if a == b:
            print((a * 2)**2)
        else:
            if max(a, b) > (min(a, b) * 2):
                print(max(a, b) ** 2)
            else:
                print((min(a, b) * 2) ** 2)
    t -= 1
except EOFError:
    pass
