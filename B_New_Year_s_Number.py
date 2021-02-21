try:
    t = int(input())
    while t:
        n = int(input())
        if n < 4041:
            print('NO')
        elif n % 2020 == 0 or n % 2021 == 0 or n % 4041 == 0:
            print('YES')
        else:
            temp = n % 4041
            if temp % 2020 == 0 or temp % 2021 == 0 or temp == 0:
                print('YES')
            else:
                print('NO')   
        t -= 1
except EOFError:
    pass
