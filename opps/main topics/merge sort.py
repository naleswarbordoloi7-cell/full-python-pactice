# divide the array into two halves, sort the two halves recursively, and then merge the sorted halves.
# Time complexity: O(n log n) in all cases
# Space complexity: O(n) due to the temporary arrays used for merging\


# step 1: divide the array into two halves
# arr = [38, 27, 43, 3, 9, 82, 10]
# left half: [38, 27, 43]
# right half: [3, 9, 82, 10]


# step 2: sort the two halves recursively (brack in two each parts)
# left half: [38, 27, 43] -> [27, 38, 43]
# right half: [3, 9, 82, 10] -> [3, 9, 10, 82]
                    # |
            #  [3,9] [82,10]
#                |      |
#               [3]  [9]   [82]  [10]

# step 3: merge the sorted halves
# merged array: [3, 9, 10, 27, 38, 43, 82]

# step 4: repeat the process until the entire array is sorted
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted array: [3, 9, 10, 27, 38, 43, 82]



def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
# copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
# checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)