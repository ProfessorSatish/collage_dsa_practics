#stack in the python
''' simple stack '''
# class file:
#     def __init__(self):
#         self.value=[]
#         print(self.value)
#     def push(self,x):
#         self.value=[x]+self.value
#         print(self.value)
#     def pop(self):
#         s=self.value.pop(0)
#         print("the delete value is  ", s)
#         print(self.value)
  
        
# s=file()
# s.push(23)
# s.push(33)
# s.push(39)
# s.push(40)
# s.pop()

# class Stacks():
#     def __init__(self):
#         self.stack=[]
#         print(self.stack)
#     def push(self,x):
#         self.stack=[x]+self.stack
#         print(self.stack)
#     def pop(self):
#         s=self.stack.pop(0)
#         print(f"The delete value is {s} ")
#         print(self.stack)
#     def display(self):
#         print(self.stack)
# r=Stacks()
# r.push(32)
# r.push(33)
# r.push(39)
# r.push(40)
# r.pop()
# r.display()
'''creating the build in funcation using the stack'''

class Stack:
    def __init__(self,size):
        self.stack=[]
        self.max_size=size 
    def push(self,x):
        if len(self.stack)>=self.max_size:
            print("Stack is overflow ")
        else:
            self.stack.append(x)
        print(f"Pushed : {x} stack is now {self.stack}")
    def remove(self):
        if len(self.stack)<=0:
            print("Stack is under flow ")
        else:
            self.data=self.stack.pop()
        print(f"pop: {self.data} now the stack is show {self.stack} ")
    def display(self):
        if len(self.stack)<=0:
            print("Stack is under flow")
        else:
            print(f"The Stack is {self.stack}")
s=Stack(5)
s.push(2)
s.push(4)
s.push(6)
s.push(3)
s.push(3)
s.display()
s.push(33)