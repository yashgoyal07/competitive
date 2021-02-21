try:
    t = int(input())
    while t:
        length = int(input())
        arr = list(map(int, input().split()))
        max_result = 0
        for i in range(length - 2):
            temp = abs(arr[i] - arr[i+1]) + abs(arr[i+1] - arr[i+2]) + abs(arr[i+2] - arr[i])
            if temp > max_result:
                max_result = temp
        print(max_result)
        t -= 1
except EOFError:
    pass