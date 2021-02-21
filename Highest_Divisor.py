try:
    n = int(input())
    max_div = 1
    for i in range(1, 11):
        if n % i == 0:
            max_div = i
    print(max_div)
except EOFError:
    pass