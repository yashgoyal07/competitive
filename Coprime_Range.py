try:
    t = int(input())
    while t:
        l, r = map(int, input().split())
        diff = r - l + 1
        while l % diff != 1:
            diff += 1
        print
        t -= 1
except EOFError:
    pass