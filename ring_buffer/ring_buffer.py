from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # adds elements to the buffer
    def append(self, item):
        self.storage.add_to_head(item)

    # returns all of the elements in the buffer in a list in their given order
    # it should NOT return any None values
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        self.current = self.storage.head
        print(self.current)
        # account for max cap
        if self.capacity == len(self.storage):
            pass
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(5)
buffer_2 = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')

print('\nbuffer length: ', buffer.storage.length)
print('\nbuffer content: ', buffer.get())
