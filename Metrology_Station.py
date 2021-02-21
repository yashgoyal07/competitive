try:
    actual_readings = list(map(int, input().split()))
    forecasted_readings = list(map(int, input().split()))
    length = len(actual_readings)
    addition = 0
    for i in range(length):
        addition += abs(actual_readings[i] - forecasted_readings[i])
    print(addition)
except EOFError:
    pass