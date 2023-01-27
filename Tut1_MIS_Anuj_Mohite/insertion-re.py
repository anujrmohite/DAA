def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n-1)
    last = arr[n-1]
    j = n-2
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j-1
    arr[j + 1] = last

def sort(arr):
    insertion_sort_recursive(arr, len(arr))
    return arr

#test
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = sort(arr)
print(sorted_arr)
