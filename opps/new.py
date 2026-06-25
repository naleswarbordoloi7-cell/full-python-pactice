class student:
    def __init__(self,name,admition_no,cgpa):
        self.name = name
        self.admition_no = admition_no
        self.__cgpa = cgpa
    def get_cgpa(self):
        return self.__cgpa
    def set_cgpa(self,cgpa):
        if cgpa<0 or cgpa>10:
            print("Invalid CGPA")
        else:
            self.__cgpa = cgpa

nale = student("nale",123,8.9)
print(nale.name)
print(nale.admition_no)
print(nale.get_cgpa())
nale.set_cgpa(8.9)
print(nale.get_cgpa())



#  find the largest element in array
def largest(arr):
    largest = arr[0]
    for num in arr:
        if num >largest:
            largest = num
    return largest
 
#  time complexity O(n)
# space complexity O(1)