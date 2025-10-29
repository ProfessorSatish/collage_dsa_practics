'''A list in python is a collection of data type that is ordered, changeable (mutable ), and allows duplicate element . It 
use to stored multiple iteam in single variable'''

#syntex
#my_list=[iteam1,iteam2,iteam3]
#ex
fruite=["apple ","banana","cherry"]
print(fruite)
#output [apple, banana, cherry]

''' some opreation in the list '''
fruite.append("mango")
print(fruite)
fruite.append("amrud")
print(fruite)
fruite.append("orange")
print(fruite)
# next opration
#insert opration insert the iteam in the specifed postion 
''' now we are creat a new list'''
a=['ram','shyam','durgesh','kailash']
#I want to insert into the shyam postion of satish name 
a.insert(1,"satish")
print(a)
print(a)
a.insert(1,"shyam")
print(a)

#remove opration
"remove the first occurance of specified iteam from the list"
b=['ram','shyam','durgesh','kailash']
# i want to remove durgesh name in the list
b.remove("durgesh")
print(b)
# i want to remove shyam name in the list
b.remove('shyam')
print(b)
# i want to remove ram name in the list
b.remove("ram")
print(b)

#pop operaton
''' remove and returns an ita at specified index default is the last iteam'''
c=['ram','shyam','durgesh','kailash']
c.pop()
print(c)
c.pop()
print(c)
c.pop()
print(c)

#extend
''' add alll element of an iterabl to the end of the list'''
d=["apple ","banana","cherry"]
e=['ram','shyam','durgesh','kailash']
f=(d.extend(e))
print(d)
d.clear()
print(d)
#index opration
s=e.index("ram")
print(s)

#count operation
g=e.count("ram")
print(g)#output 1

#reverse
s=(e.reverse())
print(s)