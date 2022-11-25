n=int(input("Enter the number to check: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes,  the number entered is in Fibonacci Series.")
    else:
        print("No, the number entered is not in Fibonacci Series.")
