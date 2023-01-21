n=int(input("enter"))
n1=0
n2=1
count=0
print("fibonacci series")
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
