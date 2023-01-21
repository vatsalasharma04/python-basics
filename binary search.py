#binary search
def binarysearch(list,n):
    low=0
    high=len(list)-1
    mid=0
    while low<=high:
        #for getting integer result
        mid =(high+low)//2
         #check if n is present at mid
        if list[mid]<n:
            low=mid+1
            #if n is greater, compare to the right of mid
        elif list[mid]>n:
            high=mid-1
        #if n is smaller, compared to the left of mid
        else:
            return mid
        #element was not present in the list
        return -1
    #initial list
    list=[12,45,78,32,36,50,54]
    n=36
    #function call
    result=binarysearch(list,n)
    if result!=-1:
        print("element is present at index", str(result))
    else:
        print("element is not present in list")
                
