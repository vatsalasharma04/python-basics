#creating bubule short function
def bubble_sort(list1):
 for i in range(0,len(list1)):
   for j in range(1,len(list1)):
     if(list1[j-1]>list1[j]):
        temp=list1[j-1]
        list1[j-1] = list1[j]
        list1[j]=temp
   return list1

list1=[5,3,8,6,7,1,4,10,909,110041]
print("Original  list is",list1)
print("sorted list is ",bubble_sort(list1))
