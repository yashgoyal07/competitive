
if __name__ == "__main__":
    t = int(input())
    while t:
        length = int(input())
        arr = list(map(int, input().split()))
        counter = 0
        flag = True
        for i in range(length-1):
            if 2 * min(arr[i], arr[i+1]) >= max(arr[i], arr[i+1]):
                flag = True
            else:
                flag = False
                break
        if not flag:
            for j in range(length-1):
                if 2 * min(arr[j], arr[j+1]) >= max(arr[j], arr[j+1]):
                    continue
                else:
                    minimum = min(arr[j], arr[j+1])
                    maximum = max(arr[j], arr[j+1])
                    while minimum * 2 < maximum:
                        counter += 1
                        minimum = minimum * 2
            print(counter)
        else:
            print(0)
        t -= 1
