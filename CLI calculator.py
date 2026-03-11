x=float(input("Enter the 1st Number:"))
y=float(input("Enter the 2nd Number:"))
print("Choose Operation:")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")
choice=input("enter the Operation:")
if choice=="1":
    Result=x+y
    print("Result:",Result)
elif choice=="2":
    Result=x-y
    print("Result:",Result)
elif choice=="3":
    Result=x*y
    print("Result:",Result)
elif choice=="4":
    if y!=0:
        Result=x/y
        print("Result:",Result)
    else:
        print("Not Divisible by Zero")
else:
    print("Invalid choice")
    
    
        
    

    
