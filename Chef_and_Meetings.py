try:
    def convert(arr, low, high):
        if arr[high] == 'AM' and arr[low] == '12':
            arr[low] = '00'
        if arr[high] == 'PM' and arr[low] != '12':
            arr[low] = str(int(arr[low]) + 12)
             
    t = int(input())
    while t:
        meeting_time = input().replace(' ', ':').split(':')
        convert(meeting_time, 0, 2)
        total_friends = int(input())
        while total_friends:
            timing = input().replace(' ', ':').split(':')
            convert(timing, 0, 2)
            convert(timing, 3, 5)
            if int(timing[0]) <= int(meeting_time[0]) <= int(timing[3]) and int(timing[1]) <= int(meeting_time[1]) <= int(timing[4]):
                print(1, end='')
            else:
                print(0, end='')
            total_friends -= 1
        print()
        t -= 1
except EOFError:
    pass


