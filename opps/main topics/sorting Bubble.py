# Bubble sort

def bubble_sort(arr):
    n = len( arr)
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n-i-1):
        # compare adjacent element
            if arr[j]> arr[j+1]:
                # swap
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr

arr =[2,3,1,4,5,6,7]
sorted_arr = bubble_sort(arr)
print(sorted_arr)


