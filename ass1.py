total=0
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
num3=int(input("enter third number :"))
num4=int(input("enter fourth number :"))
num5=int(input("enter fifth number :"))
if(num1>0 and num2>0 and num3>0 and num4>0 and num5>0):
    total=num1+num2+num3+num4+num5
    print("total count is :",total)
else:
    print("enter positive numbers")