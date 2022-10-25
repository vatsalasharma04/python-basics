print("menue driven program")

print(   "MENUE"   )
print( " to find arithmetic operations:")

print( " 1. addition")
print( " 2. substraction")
print( " 3. divide")
print( " 4. remainder")
print( " 5. multiplication")

print(" PLEASE ENTER TWO NUMBERS OF YOUR CHOICE FIRST")

a= int(input(" enter number 1:  "))
b= int(input(" enter number 2:  "))

ch=int(input("Enter your choice"))

if ch == 1:
       c=a+b
       print(" the addition is:",c)
elif ch==2:
      c=a-b
      print("the substraction is",c)
elif ch ==3:
      c=a/b
      print("the divide is",c)
elif ch == 4:
     c=a%b
     print("the remainder is",c)
elif ch==5:
     c=a*b
     print("the multiplication is",c)
else:
    print("INVALID CHOICE")
