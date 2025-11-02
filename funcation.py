#used in funcation 
def greet(name):
    return f"hello {name}"
print(greet("satish"))

def reet(name):
    return f" hello welcome to {name} in my computer world . how are your"
print(reet("satish yadav"))


#fucation with multiple  parameter
#addtion 
def add(num1, num2):
    return f" The addtion of two number num1 {num1} and num2 {num2} the sum is = {num1+num2}"
print(add(2,3))


#funcation without return void
def prtint_hello():
    print("hello")
prtint_hello()



#funcation with default argument 
def greet(name="Guest"):
    return f"hello ,{name}"
print(greet())
print(greet("rahul"))

