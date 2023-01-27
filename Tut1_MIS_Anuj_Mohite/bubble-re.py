def bubble_sort_recursive(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bubble_sort_recursive(arr, n-1)

def bubble_sort(arr):
    bubble_sort_recursive(arr, len(arr))
    return arr

# Test
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
