class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    
    def __repr__(self):
        values = []
        for val in self.iter():
            values.append(str(val))
        return " -> ".join(values)

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def append_at_a_location(self, data, index):
        node = Node(data)
        count = 1
        prev = self.head
        current = self.head

        while current:
            if index == 1:
                node.next = current
                self.head = node
                self.size += 1
                return
            elif index == count:
                prev.next = node
                node.next = current
                self.size += 1
                return
            else:
                prev = current
                current = current.next
                count += 1

    def delete_first_node(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        elif self.head is None:
            return
        else:
            current = self.head
            self.head = current.next
            self.size -= 1

    def delete_last_node(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = None
                self.tail = prev
                self.size -= 1
            prev = current
            current = current.next

words = LinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append_at_a_location('new',2)
print(words)
words.delete_first_node()
print(words)
words.delete_last_node()
print(words)
