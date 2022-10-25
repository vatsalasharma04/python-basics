#to check number is armstrong or not
num =int(input("enter the number to be checked"))
sum=0
temp=num
order=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print("it is an armstrong number", num)
else:
    print("not an armstrong number")
