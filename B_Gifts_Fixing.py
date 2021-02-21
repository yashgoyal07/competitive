try:
    t = int(input())
    while t:
        counter = 0
        length = int(input())
        candies = list(map(int, input().split()))
        oranges = list(map(int, input().split()))
        min_candies = min(candies)
        min_oranges = min(oranges)
        for i in range(length):
            if (candies[i]-min_candies) == (oranges[i]-min_oranges):
                counter += (candies[i]-min_candies)
            else:
                counter += max((candies[i]-min_candies), (oranges[i]-min_oranges))
        print(counter)
        t -= 1
except EOFError:
    pass
