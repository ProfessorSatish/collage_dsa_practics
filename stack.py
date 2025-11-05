#stack in the python
''' simple stack '''
class stack:
    def __init__(self):
        self.value=[]
        print(self.value)
    def push(self,x):
        self.value=[x]+self.value
        print(self.value)
    def pop(self):
        return self.value.pop(0)
        
s=stack()
s.push(23)
s.push(33)
s.push(39)
s.pop()
print(s.value)
s.pop()
print(s.value)
'''creating the build in funcation using the stack'''
