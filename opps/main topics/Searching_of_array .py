# check elememt one by one (linear)
arr = [1,2,3,5,6]
target = 5

for i in range(len(arr)):
    if arr[i] ==  target:
        print("element found at index",i)
        break
else :
    print ("element not found")

# funtion version
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
        
arr =[1,2,4,5,6,7,]
print(linear_search(arr,5))


# Binary Search

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low  <= high:
        mid =(low + high)//2
        if arr[mid]== target:
            return mid
        elif arr[mid] <target:
            low = mid +1
        else:
            high = mid -1
        return -1
    arr =[10,20,3,5,60]
    print(binary_search(arr,5))
    # O(logn)  f(n) = log2 n
    