#a compony insures drivers
a=str(input("enter your marital status(married/unmarried):"))
b=str(input("enter your sex (male/female):"))
c=int(input("enter your age:"))
if a=='married':
    print("driver is insured")
elif a=='unmarried' and b=='male' and c> 30:
    print("driver is insured")
elif a=='inmarried' and b== 'female' and c> 25:
         print("driver is insured")
else:
    print("driver is not insured")
