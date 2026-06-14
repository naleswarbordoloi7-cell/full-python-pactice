# word -meaning
# name -naleswar
# age -21
# college-sviet

student ={"name":"naleswar","age":19,"brinch":"csd"}
print(student)
print(student["name"])
print(student["age"])
print(student["brinch"])


# add new value
student["collge"] ="sviet"
print(student)

# updating values
student["brinch"] = 'cse'
print(student)

# removing items using pop()
student.pop("age")
print(student)

# dictionary methode
print(student.keys())
print(student.values())
print(student.items())

# use loops

for key,value in student.items():
    print(key,":",value)

# count how many times each element appears
number = (1,2,2,3,3,4)
freq = {}
for num in number:
    freq[num] = freq.get(num,0)+1
print(freq)

