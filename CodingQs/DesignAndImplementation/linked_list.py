class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def insert(self, index, value):
      if index == 0:
        self.prepend(value)
      elif index > self.length:
        self.append(value)
      else:
        curr = self.head
        for _ in range(index-1):
          curr = curr.next
        node = Node(value)
        node.next = curr.next
        curr.next = node
        return self

    def remove(self, index):
        if index == 0:
          self.head = self.head.next
          self.length -= 1
          return self
        elif index > self.length:
          return self
        
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        deleted = curr.next
        curr.next = curr.next.next
        del deleted
        self.length -= 1
        return self

    def print(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next

        print(vals)

class Node2:
  def __init__(self, value) -> None:
      self.value = value
      self.next = None
      self.prev = None


class DoublyLinkedList():
    def __init__(self, value):
        self.head = Node2(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node2(value)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1
        return self

    def prepend(self, value):
        node = Node2(value)
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def insert(self, index, value):
      if index == 0:
        self.prepend(value)
      elif index > self.length:
        self.append(value)
      else:
        curr = self.head
        for _ in range(index-1):
          curr = curr.next
        node = Node2(value)
        node.next = curr.next
        curr.next = node
        node.prev = curr
        node.next.prev = node
        return self

    def remove(self, index):
        if index == 0:
          self.head = self.head.next
          self.length -= 1
          return self
        elif index > self.length:
          return self
        
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        deleted = curr.next
        curr.next = curr.next.next
        curr.next.prev = curr
        del deleted
        self.length -= 1
        return self

    def print(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next

        print(vals)

llist = LinkedList(10)
llist.append(5)
llist.append(16)
llist.prepend(1)
llist.insert(2, 500)
llist.remove(1)
print(llist.head.next.value)

  


