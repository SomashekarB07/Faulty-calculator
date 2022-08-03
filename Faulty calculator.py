a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
operator = input("Enter the operator :")

if operator=='+':
    if((a==56 and b==6) or (a==6 and b==56)):
        print(f"Sum of {a} and {b} = {77}")
    else:
        print(f"Sum of {a} and {b} = {a+b}")
elif operator=='-':
    if((a==77 and b==15) or (a==15 and b==77)):
        print(f"Substraction of {a} and {b} = {52}")
    else:
        print(f"Substraction of {a} and {b} = {a-b}")
elif operator=='*':
    if((a==45 and b==3) or (a==3 and b==45)):
        print(f"Multipication of {a} and {b} = {555}")
    else:
        print(f"Multipilcation of {a} and {b} = {a*b}")
elif operator=='/':
    if((a==56 and b==6) or (a==6 and b==56)):
        print(f"Division of {a} and {b} = {6.54}")
    else:
        print(f"Division of {a} and {b} = {a/b}")
elif operator=='**':
    if((a==4 and b==3) or (a==3 and b==4)):
        print(f"Power of {a} and {b} = {56}")
    else:
        print(f"Power of {a} and {b} = {a**b}")
else:
    print("INVALID KEY PLEASE TRY AGAIN")
