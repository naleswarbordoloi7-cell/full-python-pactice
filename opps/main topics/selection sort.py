# find the smallest element and place it at the beginning of the array
# Time complexity: O(n^2) in all cases
# Space complexity: O(1) because it is an in-place sorting algorithm    

# step 1: find the smallest element in the array
# arr = [64, 25, 12, 22, 11]
# smallest element: 11

# step 2: swap the smallest element with the first element of the array
# arr = [11, 25, 12, 22, 64]    

# step 3: repeat the process for the remaining unsorted elements
# arr = [11, 25, 12, 22, 64]
# smallest element: 12

# swap the smallest element with the second element of the array
# arr = [11, 12, 25, 22, 64]

# repeat the process for the remaining unsorted elements
# arr = [11, 12, 25, 22, 64]
# smallest element: 22

# swap the smallest element with the third element of the array
# arr = [11, 12, 22, 25, 64]



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print(f"considering sub-array: {arr[i:n]}, starting index: {i}, current minimum index: {min_index}")
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"new minimum found: {arr[min_index]} at index {min_index}")
        # swap the found minimum element with the first element
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr
arr =[11, 12, 25, 22, 64]
print(selection_sort(arr))