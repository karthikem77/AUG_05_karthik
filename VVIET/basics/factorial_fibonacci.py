'''
num = int(input("enter a number is"))
factorial = 1
if num < 0:
   print(" factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
'''
'''
# FOR NEGATIVE FACTORIAL
num = int(input("enter a number is"))
factorial = 1
while(num < 0):
   print(" enter valid number")
   num=int(input("enter a number"))
if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
'''
'''
#  Fibonacci sequence up to n-th term

nterms = int(input("enter the number "))
n1, n2 = 0, 1
count = 0
while(nterms <= 0):
   print(" enter valid number")
   nterms = int(input("enter number")) 
if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1
'''
'''
for x in range(8):
    print(x)
    if x == 4:
        break
print("execution completed")
'''
'''
for x in range(8):
    print(x)
    if x == 3:
        print("x is 3")
        continue
print("execution completed")
'''
'''
#for even or odd number
for x in range(8):
    if x%2 == 0:
        print(x*2)
        continue
    else:
        print(x)
print("execution completed")
'''    


