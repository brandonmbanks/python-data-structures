import unittest
from singly_linked_list.node import Node
from singly_linked_list.linked_list import LinkedList


class SinglyLinkedListTest(unittest.TestCase):

    def test_it_should_create_singly_linked_list_with_a_head_node(self):
        head = Node(value='value')
        linked_list = LinkedList(head)
        self.assertEqual('value', linked_list.head.value)

    def test_it_should_add_a_new_node_to_the_end_of_the_singly_linked_list(self):
        head = Node(value='head')
        linked_list = LinkedList(head)
        new_node = Node(value='new node')
        linked_list.add_node(new_node)
        self.assertEqual('new node', linked_list.head.next_node.value)

    def test_it_should_delete_a_node_when_it_exists_and_return_1(self):
        head = Node(value='head')
        linked_list = LinkedList(head)
        self.assertEqual(1, linked_list.size())
        response = linked_list.delete('head')
        self.assertEqual(0, linked_list.size())
        self.assertEqual(1, response)

    def test_it_should_return_0_when_trying_to_delete_a_node_that_does_not_exist(self):
        linked_list = LinkedList()
        response = linked_list.delete('head')
        self.assertEqual(0, response)
