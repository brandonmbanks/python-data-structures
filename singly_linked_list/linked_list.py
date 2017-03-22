class LinkedList():

    def __init__(self, head=None):
        self.head = head
        self.last = head

    def add_node(self, new_node):
        '''
        it appends a node to the end of the list
        if the size of the list is 0 it appends to the head
        '''
        if self.size() == 0:
            self.head = new_node
            self.head.next_node = new_node
            self.last = new_node
        else:
            self.last.next_node = new_node
            self.last = new_node

    def size(self):
        '''
        returns the size of the singly linked list
        '''
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next_node
        return size

    def search(self, value):
        '''
        returns the node with the search value
        returns 0 if can't find the value
        '''
        current = self.head
        while current:
            if value == current.value:
                return current
            current = current.next_node
        return 0

    def delete(self, value):
        '''
        deletes the first node with the value and returns 1
        returns 0 if can't find the value
        '''
        current = self.head
        previous = None
        while current:
            if value == current.value:
                if previous:
                    previous.set_next_node(current.next_node)
                else:
                    self.head = current.next_node
                return 1
            previous = current
            current = current.next_node
        return 0
