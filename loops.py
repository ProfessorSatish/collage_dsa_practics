#loops in the 
for i in range(1,11):
    print(i)
#table in the for loops 
t=int(input("Enter the number that you want to table "))
for i in range(1,11):
    print(f"{t} x {i} = {t*i}",)


#while loops
# print the table fro the while loops of help
s=int(input("Enter the number that you want to table "))
i= 1
while i<=10:
    print(f"{s} x {i} ={s*i}")
    i+=1

#break statement
for i in range(1,6):
    if (i==2):
        break
    print(i)

#Continue statement
for i in range(1,6):
    if(i==5):
        continue
    print(i)

for i in range(1,6):
    if (i==2):
        pass
    print(i)


#if elif else and the break and continue statement
for i in range(1,6):
    if i==2:
        print("skipping ",i)
        continue
    elif(i==5):
        break
    else:
        print("Number is ",i)