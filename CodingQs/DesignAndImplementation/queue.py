from linked_list import LinkedList


class queue():
    def __init__(self, value) -> None:
        self._queue = LinkedList(value)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if not self._queue.head:
            return None
        value = self._queue.head.value
        self._queue.head = self._queue.head.next
        return value

    def peek(self):
        return self._queue.head.value


        
