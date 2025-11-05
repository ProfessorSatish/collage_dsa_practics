class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        New_node=Node(data)
        New_node.next=self.top
        self.top=New_node
        print(f"push the data {data}")

    def pop(self):
        if self.top is None:
            print("stack is under flow")
            return
        removed= self.top.data
        self.top=self.top.next
        print(f" popped {removed}")

    def display(self):
        if self.top is None:
            print("stack is emty")
            return
        temp=self.top
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()