arr = []
n = int(input("Enter number of elements : "))
print("enter the elements: ")
for i in range(0, n):
    ele = int(input())
    arr.append(ele) 
uni_arr = []
for element in arr:
    if element not in uni_arr:
        uni_arr.append(element)
print("Original List of Numbers :", arr)
print("Array after removing duplicates Number", uni_arr)
