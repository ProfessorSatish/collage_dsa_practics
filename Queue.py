# class Queue:
#     def __init__(self):
#         self.value=[]
#     def enqueue(self,x):
#         self.value.append(x)
#         print(self.value)
#     def dequeue(self):
#         data=self.value.pop(0)
#         print(f" the value is delete is {data}  and now queue is like that {self.value}")
#     def display(self):
#         print(self.value)
# s=Queue()
# s.enqueue(23)
# s.enqueue(29)
# s.enqueue(22)
# s.enqueue(99)
# s.enqueue(100)
# s.dequeue()
# s.display()

''' class method to queue code that add, remove and display element '''
# class Queue:
#     def __init__(self,size):
#         self.queue=[]
#         self.max_size=size
#     def enqueue(self,x):
#         if len(self.queue)>=self.max_size:
#             print(" Queue is overflow")
#             return
#         self.queue.append(x)
#         print(f"{x} that element add in the queue and {self.queue}")
#     def dequeue(self):
#         if not self.queue:
#             print("Queue is under flow ")
#             return
#         s=self.queue.pop(0)
#         print(f"{s} element is delete now {self.queue}")
#     def is_empty(self):
#             if len(self.queue)==0:
#                  print("yes Queue is empty")
#                  return
# d=Queue(5)
# d.is_empty()
# d.enqueue(33)   
# d.enqueue(323)
# d.enqueue(55)
# d.enqueue(200)
# d.dequeue()
# d.is_empty()
# d.dequeue()
# d.dequeue()
# d.dequeue()
# d.dequeue()
# d.is_empty()

''' logical implementation of the queue'''
class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.rear==self.size-1:
            print("Queue is overflow")
            return
        if self.front==-1:
            self.front=0
            
            
        self.rear+=1
        self.queue[self.rear]=data
        print(f"Enqued {data}")
        print(self.queue)

    def dequeue(self):
        if self.front==-1:
            print("queue is underflow")
            return
        value=self.queue[self.front]
        self.front +=1
        print(f"Delete the {value}")
    def peek(self):
        if self.queue==-1:
            print("queue is under flow")
            return
        print(f"The element is {self.front}")
    def display(self):
        if self.front==-1 or self.front>self.rear:
            print("queue is empty")
            return
        print("Queue (front ->rear)" ,end=" ")
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end =" ")
        print()
    

b=Queue(5)
b.enqueue(33)
b.enqueue(23)
b.enqueue(99)
b.enqueue(100) 
b.dequeue()     
b.display()
b.dequeue()
