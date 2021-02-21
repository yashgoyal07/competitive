if __name__ == "__main__":
    t = int(input())
    while t:
        length = int(input())
        arr = list(map(int, input().split()))
        c0 = 0
        c1 = 0
        c2 = 0
        counter = 0
        for i in range(length):
            if arr[i] % 3 == 0:
                c0 += 1
            elif arr[i] % 3 == 1:
                c1 += 1
            else:
                c2 += 1
        while not (c0 == c1 == c2):
            maximum = max(c0, c1, c2)
            if maximum == c0:
                counter += 1
                c0 -= 1
                c1 += 1
            elif maximum == c1:
                counter += 1
                c1 -= 1
                c2 += 1
            else:
                counter += 1
                c2 -= 1
                c0 += 1
        print(counter)
        t -= 1