def selection_sort(arr):
    n = len(arr)
    
    # Move the boundary of the unsorted subarray
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
nums = [64, 25, 12, 22, 11]
print("Selection Sort Result:", selection_sort(nums))