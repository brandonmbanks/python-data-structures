class Node():

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node
