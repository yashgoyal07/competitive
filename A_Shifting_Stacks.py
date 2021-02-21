if __name__ == '__main__':
    t = int(input())
    while t:
        length = int(input())
        arr = list(map(int, input().split()))
        for i in range(length-1):
            temp = arr[i] - i
            if temp > 0:
                arr[i+1] = arr[i+1] + temp 
            else:
                break
        if temp > 0 or arr[-1] > arr[-2]:
            print('YES')
        else:
            print('NO')
        t -= 1
