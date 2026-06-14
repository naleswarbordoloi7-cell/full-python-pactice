# an array is a collection of elements stored in contiguous memory location


# travering an array
arr = [10,20,30,40]
for i in arr:
    print(i)
# O(n) f(n)=n


# Accessing Elements
 
arr = [1,2,3,4,5]
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
# O(1)

# Inserting an elements add using append

arr =[1,2,3,4]
arr.append(5)
print(arr)
# average O(1)

arr =[1,2,3]
arr.insert(1,20)
print(arr)
# O(n)

# Deletion an element using remove
arr = [1,2,3,4,5]
arr.remove(3)
print(arr)
# O(n)

# Searching in an Array
# \\ linera search

arr=[1,2,3,4]
target = 3
for i in range(len(arr)):
    if arr[i] ==target:
        print("found at index",i)
        break





# find the largest element
arr =[10,20,80,30,40,50]
largest = arr[0]
for num in arr :
    if num >largest:
        largest = num

print("largest:",largest)




# Find the smallest element
arr = [10,20,30,5,40,50]
smallest = arr[0]
for num in arr:
    if num< smallest:
        smallest = num
print("smalest:",smallest)


# revese the array
arr =[1,2,3,4,6,5]

print(arr[::-1])

# find the sum of all number
arr =[10,20,30,40]
total = 0
for num in arr:
    total += num
print("sum =",total)



# count even number in array
arr =[1,2,3,4,5,6]
count = 0
for num in arr:
    if num % 2==0:
        count += 1
print("even number =",count)



# optimized Approch 

arr = [10,20,50,40]

largest = secound = float('-inf')
for num in arr:
    if num > largest:
        secound = largest
        largest = num
    elif num > secound and num != largest:
         secound = num
print("second largest=",secound)


arr =[1,2,3,4]
print(arr)
arr_2 =[x*2 for x in range(1,5)]
print(arr_2)
arr_3=list(range(1,8))
print(arr_3)