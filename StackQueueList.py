MAX_SIZE = 100

# Stack implementation using fixed-size array
class Stack:
    def __init__(self):
        self.arr = [None] * MAX_SIZE
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == MAX_SIZE - 1

    def push(self, val):
        if not self.is_full():
            self.top += 1
            self.arr[self.top] = val
        else:
            print("Stack Overflow!")

    def pop(self):
        if not self.is_empty():
            val = self.arr[self.top]
            self.top -= 1
            return val
        else:
            print("Stack Underflow!")
            return -1

    def peek(self):
        if not self.is_empty():
            return self.arr[self.top]
        else:
            print("Stack is empty!")
            return -1

# Queue implementation using fixed-size array
class Queue:
    def __init__(self):
        self.arr = [None] * MAX_SIZE
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % MAX_SIZE == self.front

    def enqueue(self, val):
        if not self.is_full():
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % MAX_SIZE
            self.arr[self.rear] = val
        else:
            print("Queue Overflow!")

    def dequeue(self):
        if not self.is_empty():
            val = self.arr[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % MAX_SIZE
            return val
        else:
            print("Queue Underflow!")
            return -1

    def peek(self):
        if not self.is_empty():
            return self.arr[self.front]
        else:
            print("Queue is empty!")
            return -1

# Singly linked list implementation using fixed-size array
class LinkedList:
    class Node:
        def __init__(self, val=0, next_index=-1):
            self.data = val
            self.next = next_index

    def __init__(self):
        self.arr = [self.Node() for _ in range(MAX_SIZE)]
        self.head = -1
        self.tail = -1
        self.free_index = 0
        for i in range(MAX_SIZE - 1):
            self.arr[i].next = i + 1
        self.arr[MAX_SIZE - 1].next = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.free_index == -1

    def insert_front(self, val):
        if not self.is_full():
            new_index = self.free_index
            self.free_index = self.arr[self.free_index].next
            self.arr[new_index] = self.Node(val)
            if self.is_empty():
                self.head = self.tail = new_index
            else:
                self.arr[new_index].next = self.head
                self.head = new_index
        else:
            print("List Overflow!")

    def remove_front(self):
        if not self.is_empty():
            val = self.arr[self.head].data
            temp = self.head
            self.head = self.arr[self.head].next
            self.arr[temp].next = self.free_index
            self.free_index = temp
            if self.head == -1:
                self.tail = -1
            return val
        else:
            print("List Underflow!")
            return -1

# Main function
if __name__ == "__main__":
    # Stack example
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top element of the stack:", stack.peek())

    print("Popping elements from the stack:", end="")
    while not stack.is_empty():
        print(" ", stack.pop(), end="")
    print()

    # Queue example
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front element of the queue:", queue.peek())

    print("Dequeueing elements from the queue:", end="")
    while not queue.is_empty():
        print(" ", queue.dequeue(), end="")
    print()

    # Singly linked list example
    linked_list = LinkedList()
    linked_list.insert_front(1)
    linked_list.insert_front(2)
    linked_list.insert_front(3)

    print("Removing elements from the front of the list:", end="")
    while not linked_list.is_empty():
        print(" ", linked_list.remove_front(), end="")
    print()
