# process of store and organize data.
# Types :
#1.list - []
#2.tuples - ()
#3.sets - {elements}
#4.dictionaries - {key-value-pairs}
'''
a=[]
b=()
c={1,2}
d={1:1,2:2,3:3}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
'''
1. Define list: using [],built-fn 'list'
2. I can create empty list
3. Access:index,slicing operators
4.reverse list: using -1 as step in slicing operator
5.list accept duplicate values
6.list is heterogeneous
'''
'''
a=[1,2,3,4,"abc"]
b=[]
c=list(range(6))
print(a)
print(b)
print(c)
print(a[0]) #index
print(c[0:4:2]) #slicing operator
print(c[::-1])
'''
 
#1. list is mutable(we cant store fixed objects in list)

'''
a=[1,2,3,4,"abc"]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
print(a)
a[2]=9
print(a)
'''
'''
a=[1,2,3,4,"abc",1,2]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
print(a)
a[2]=9
print(a)
print(len(a))
print(a.count(1))
'''
#1.count the accrance of each element in given list
'''
a=[1,2,3,4,"abc",1,2]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
print(a)
a[2]=9
for x in a:
    print(x)
'''
'''
# add element
a=[1,2,3,4,"abc",1,2]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
a.append(10)
print(a)
a.append(c)
print(a)
'''
'''
# copy element
a=[1,2,3,4,"abc",1,2]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
d=a.copy()
print(d)
'''
a=[1,2,3,4,"abc",1,2]
b=[]
c=list(range(6))
weekdays=["mon","tue",""]
a.extend(c)
print(a)
print(a[11])