'''
Types:
conditional statements- if,ifelse,nested ifelse,series if else
looping statements- for,while,do-while,while-do
sequential flow
'''
a=1
b=2
if b>1:
    if a<2:
        a=a+1
        print(a)
elif a !=0:
    print("this is else block")
    
print("End of the program")
'''
largest of three number
'''
''''a=4
b=5
c=7
if c>5:
    if a<5:
        print(b)
if c>b:
    print(c+1)
'''
#example program for largest three number

a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
output=a+b+c
print("the sum is",output)
#print(type(a))
#print(type(b))
if a>=b and a>=c:
    print("largest number is" ,a)
elif b>=c and b>=a:
    print("largest number is" ,b)
else:
    print("largest number is" ,c)
    

    

