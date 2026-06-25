arr =[1,3,4,56,6]
print(arr[::-1])

# traing zeroes to end of array
arr =[1,0,2,0,3,0,4]
def move_zeroes(arr):
    n = len(arr)
    count =0
    for i in range(n):
        if arr[i] !=0:
            arr[count] = arr[i]
            count +=1

    while count < n:
        arr[count] =0
        count +=1
move_zeroes(arr)
print(arr)  

arr=[1,0,2,3,0,4]
n=len(arr)
k=0
for i in range(n):
    if arr[i]!=0:
        arr[i],arr[k]=arr[k],arr[i]
        k+=1
print(arr)