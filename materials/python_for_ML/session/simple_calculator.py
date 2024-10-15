x=float(input("first number "))
y=float(input("second number "))
z=input("enter the sign ")
if z=="+":
    result=x+y
    print(result)
elif z=="-":
    result=x-y
    print(result)
elif z=="*":
    result=x*y
    print(result)
elif z=="/":
    result=x/y
    print(result)
else:
    print("please try again")    