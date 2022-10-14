class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_at_start(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1

    def append_at_a_location(self, data):
        node = Node(data)
        current = self.head
        prev = current

        while current:
            if current.data == node.data:
                node.prev = prev
                node.next = current
                prev.next = node
                current.prev = node
                self.count += 1
            prev = current
            current = current.next

    def iter(self):
        current = self.head
        while current:
            val = current
            current = current.next
            yield val.data

    def contains(self, data):
        for node_data in self.iter():
            if node_data == data:
                return True
        return False

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    if current.next is None:
                        self.tail = None
                        self.head = None
                        self.count = 0
                    else:
                        current.next.prev = None
                        self.head = current.next
                        self.count -= 1
                elif current == self.tail:
                    current.prev.next = None
                    self.tail = current.prev
                    self.count -= 1
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.count -= 1
            current = current.next

    def __repr__(self):
        items = []
        for node_data in self.iter():
            items.append(str(node_data))
        return " <-> ".join(items)

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.append(6)
dllist.append(7)
dllist.append(8)

print(dllist)
dllist.append_at_start(100)
print(dllist)
dllist.append_at_a_location(8)
print(dllist)
print(dllist.contains(3))
print(dllist.contains(89))
print(dllist)
dllist.delete(1)
print(dllist)
dllist.delete(6)
print(dllist)
dllist.delete(8)
print(dllist)

