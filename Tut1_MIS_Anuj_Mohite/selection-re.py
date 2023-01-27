def selection_sort_recursive(arr, n, index=0):
    if index == n:
        return
    min_idx = index
    for i in range(index+1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[index], arr[min_idx] = arr[min_idx], arr[index]
    selection_sort_recursive(arr, n, index+1)

def selection_sort(arr):
    selection_sort_recursive(arr, len(arr))
    return arr

# Test
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
