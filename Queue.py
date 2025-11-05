class Queue:
    def __init__(self):
        self.value=[]
    def enqueue(self,x):
        self.value.append(x)
        print(self.value)
    def dequeue(self):
        data=self.value.pop(0)
        print(f" the value is delete is {data}  and now queue is like that {self.value}")
    def display(self):
        print(self.value)
s=Queue()
s.enqueue(23)
s.enqueue(29)
s.enqueue(22)
s.enqueue(99)
s.enqueue(100)
s.dequeue()
s.display()

