from linked_list import LinkedList

class stackList:
    def __init__(self, value):
        self._stack = LinkedList(value)

    def push(self, value):
        self._stack.prepend(value)
        return self

    def pop(self):
        if not self._stack.head:
            return None
        value = self._stack.head.value
        self._stack.head = self._stack.head.next
        return value

    def peek(self):
        return self._stack.head.value

class stackArray:
    def __init__(self, value):
        self._stack = [value]

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        if not self._stack:
            return None
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]