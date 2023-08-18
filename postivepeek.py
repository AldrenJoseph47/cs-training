n=int(input(print("Enter the number of elements : ")))
arr=[]
print("enter values :")
for i in range (n):
    arr.append(int(input()))
for i in range(len(arr)):
    if (i == 0 or arr[i] > arr[i - 1]) and (i == len(arr) - 1 or arr[i] > arr[i + 1]):
        print("postive peek elements : ",arr[i]," at index : ",i)
        break
            
                                                                                                                                
