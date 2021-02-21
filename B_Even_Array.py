try:
    t = int(input())
    while t:
        length = int(input())
        arr = list(map(int, input().split()))
        even_odd = 0
        odd_even = 0
        for index, element in enumerate(arr):
            if element % 2 != 0 and index % 2 == 0:
                even_odd += 1
            elif element % 2 == 0 and index % 2 != 0:
                odd_even += 1
        if even_odd == odd_even:
            print(even_odd)
        else:
            print(-1)
        t -= 1
except EOFError:
    pass
