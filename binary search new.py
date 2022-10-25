
def binary_search(list1, n):  
    start = 0  
    end = len(list1) - 1  
    mid = 0  
  
    while start<=end:  
        mid = (start + end) // 2  
  
        if list1[mid] < n:  
            end = mid - 1  

        elif list1[mid] > n:  
            start = mid + 1  
  
        else:
             return mid  
  
        return -1

a=int(input("enter no of element"))
list1=list()
for i in range (a):
    item= int(input("enter element"))
    list1.append(item)
print("list: ",list1)

n=int(input("enter element to be searched"))
result = binary_search(list1, n)

  
if (result != -1):  
    print("Element is  present")  
else:  
    print("Element is not present in list")
