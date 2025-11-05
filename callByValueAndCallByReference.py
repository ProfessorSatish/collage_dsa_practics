# #call by referance
# def modify(x):
#     x=x+5
#     print("inside funcation",x)
# num=10
# modify(num)
# print("outside the funcation ",num)

# #another funcation
# def su(nums):
#     nums=nums*5
#     print("x is inside the funcation",nums)
# nums=23
# su(nums)
# print("outer side the funcation ",nums)

# # one another funcation
# def sumb(x):
#     x=x+100
#     print("Inside the funation x ",x)
# numsb=23
# sumb(33)
# print("outer side the funcation numbs ",numsb)


# #call by reference
# def modify(lst):
#     lst.append(4)
#     print("inside funcation ",lst)
# my_list=[2,4,6]
# sc_list=[3,6,9]
# modify(my_list)
# modify(sc_list)
# print(sc_list)

#example using both

def modify_value(a,b):
    a=a+5
    b.append(4)
    print("Inside funcation -a:",a)
    print("Inside funcation -b: ",b)
num=10
my_list=[1,2,3]
modify_value(num,my_list)
print("the outside the funcaiton ",num)
print("The outside the list ",my_list)