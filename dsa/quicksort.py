''' Quick Sort Implementation '''

def quick(arr, l, r):
    pivot = arr[l]
    left = l+1
    right = r
    
    while True:
        while pivot <= arr[right] and right >= left:
            right -= 1

        while pivot >= arr[left] and right >= left:
            left += 1

        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
        
    arr[l], arr[right] = arr[right], arr[l]
    return right

def quicksort(arr, l, r):
    if l<r:
        p = quick(arr, l, r)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)

arr = [20, 10, 40, 50, 30]
quicksort(arr, 0, len(arr)-1)
print(arr)
