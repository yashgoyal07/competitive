try:
    t = int(input())
    while t:
        s = int(input())
        intro_arr = list(map(int, input().split()))
        sum_epi_min = 0
        i = 0
        while s:
            arr = list(map(int, input().split()))
            e = arr[0]
            episode_arr = arr[1:]
            for item in episode_arr:
                sum_epi_min += (item - intro_arr[i]) 
            i += 1
            s -= 1
        print(sum_epi_min + sum(intro_arr))
        t -= 1
except EOFError:
    pass
