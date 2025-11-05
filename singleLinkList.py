# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at front")

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at end (list was empty)")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end")

    def deleteFirstNode(self):
        if self.head is None:
            print("List is empty, cannot delete")
            return
        removed = self.head.data
        self.head = self.head.next
        print(f"Deleted first node: {removed}")

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        print("Linked List: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Driver Code
l = LinkedList()
l.insertFront(22)
l.insertFront(223)
l.insertEnd(90)
l.display()
l.deleteFirstNode()
l.display()
