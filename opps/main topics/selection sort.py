# find the smallest element and place it at the beginning of the array
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the found minimum element with the first element
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr
arr =[2,5,8,6,5,4,9,3]
print(selection_sort(arr))