import array



arr2=array.array('i',[10,20,30,40,50,60])
arr = array.array('i', [1, 2, 3, 4])   
print(arr)

print(arr[1])
print(arr[2])
print(arr[3])
print(arr[0])

arr.insert(1,23)
print(arr)
arr.insert(2,99)
print(arr)
arr.insert(3,10000)
print(arr)
arr.insert(5,5000)
print(arr)


#remove the element
# arr.remove(23)
# print(arr)
# arr.remove(2)
# print(arr)
# arr.remove(5000)
# print(arr)
# arr.remove(10000)
# print(arr)

#pop opration


# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.pop(0)
# print(arr)
# arr.pop(0)
# print(arr)

print(len(arr))
print(arr[3:6])

#reverse
print(arr[: : -1])

#serching 
print(arr.index(3))

arr.extend(arr2)
print(arr)

print(arr.count(3))
