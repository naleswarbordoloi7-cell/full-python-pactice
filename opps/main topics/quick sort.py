# choose a pivot element and partition the array around it
# Time complexity: O(n log n) on average, O(n^2) in the worst case (when the smallest or largest element is always chosen as the pivot)
# Space complexity: O(log n) on average, O(n) in the worst case 

# step 1: choose a pivot element (e.g., the middle element of the array)
# arr = [3, 6, 8, 10, 9, 1, 2, 1]
# pivot = 10 
#    
# step 2: partition the array around the pivot
# left: [3, 6, 8, 9, 1, 2, 1]
# middle: [10]
# right: []

# step 3: recursively apply the same process to the left and right sub-arrays
# left: [3, 6, 8, 9, 1, 2, 1] -> pivot = 9
# left: [3, 6, 8, 1, 2, 1]  

# step 4: combine the sorted sub-arrays and the pivot to get the final sorted array
# sorted array: [1, 1, 2, 3, 6, 8, 9, 10]       


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [3, 6, 8, 10, 9, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)