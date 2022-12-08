def check(x):
    a,b,c=0,1,0
    if x==0 or x==1:
        print(x,"YES!")
    else:
        while c<x:
            c=a+b
            
            b=a
            
            a=c
            
        if c==x:
            print(x,":YES!, the number is there in the series.")
        else:
            print(x,":NO!, the number is there in the series.")
a=int(input("How many number u want to enter one number or more than then one number to check in the seriesIf u want to inpur one number enter 1 or else enter any number: "))
if a==1:
      n=int(input("enter only one number: "))
      check(n)
else:
    d=list(eval(input("enter more than one number: ")))
    for i in d:
        check(i)
