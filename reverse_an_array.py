# # Brute Force Method

# arr = list(map(int, input().split()))
# result = []
# length = len(arr)
# for i in range(length):
#     result.append(arr[length - 1 - i])
# print(result)


# # Iterative Way

# arr = list(map(int, input().split()))
# length = len(arr)
# for i in range(length//2):
#     arr[i], arr[length-1-i] = arr[length-1-i], arr[i]
# print(arr)


# # Iterative Way with While loop

# arr = list(map(int, input().split()))
# result = []
# start = 0
# end = len(arr) - 1
# while start < end:
#     arr[start], arr[end] = arr[end], arr[start]
#     start += 1
#     end -= 1
# print(arr)


# # Recursive Way

# arr = list(map(int, input().split()))
# length = len(arr)
# start = 0
# end = length - 1
# def reverse_arr(arr, start, end):
#     if start >= end:
#         return
#     arr[start], arr[end] = arr[end], arr[start]
#     reverse_arr(arr, start+1, end-1)
# reverse_arr(arr, start, end)
# print(arr)


# list slicing Way

arr = list(map(int, input().split()))
arr = arr[::-1]
print(arr)