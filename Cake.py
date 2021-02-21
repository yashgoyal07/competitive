#### Here, only Binary Search in remaining. Linear search 
#### increasing time to execution. Because here array is an 
#### index array that's why don't need to sort that. 

#### Please Learn Binary search and re-write again this code.

try:
    t = int(input())
    while t:
        arr = list(map(int, list(input())))
        ind_arr = []
        for i in range(len(arr)):
            if arr[i] == 1:
                ind_arr.append(i+1)
        result = []
        d = 0
        ind_arr.sort()
        while d < len(arr):
            counter = 0
            for j in range(len(ind_arr)):
                if (ind_arr[j] + d) in ind_arr[j:]:
                    counter += 1
            result.append(counter)
            d += 1
        for element in result:
            print(element, end=' ')
        t -= 1
except EOFError:
    pass

