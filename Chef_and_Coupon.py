try:
    t = int(input())
    while t:
        d, c = map(int, input().split())
        order_1 = list(map(int, input().split()))
        order_2 = list(map(int, input().split()))
        sum_order_1 = sum(order_1)
        sum_order_2 = sum(order_2)
        total_delivery = sum_order_1 + sum_order_2 + (d * 2)
        if sum_order_1 < 150:
            sum_order_1 += d
        if sum_order_2 < 150:
            sum_order_2 += d
        total_coupan = sum_order_1 + sum_order_2 + c
        if total_coupan < total_delivery:
            print('YES')
        else:
            print('NO') 
        t -= 1
except EOFError:
    pass