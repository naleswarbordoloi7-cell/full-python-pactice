number_set = {1,1,2,2,3,3}
print(number_set) 
# it removes the same values


# add number
number_set.add(4)
print(number_set)


# remove number
number_set.remove(2)
print(number_set)

# lenth of set
print(len(number_set))

# membership check
print(10 in number_set)
print(1 in number_set)

a ={1,2,3}
b ={3,5,6}
print(a|b)
print(a & b)
print(a-b)