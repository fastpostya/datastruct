import unittest
from utils.node import Node
from utils.stack import Stack


class Test_Stack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.node_10 = Node(10)
        self.node_20 = Node(20)
        self.node_30 = Node(30)

    def test_stack__init__(self):
        self.assertEqual(Node(10).data, self.node_10.data)

    def test_push(self):
        self.stack.push(self.node_10)
        self.stack.push(self.node_20)
        self.assertEqual(len(self.stack.elements), 2)

    def test_pop(self):
        self.stack.push(self.node_10)
        self.stack.push(self.node_20)
        self.stack.push(self.node_30)
        self.assertEqual(len(self.stack.elements), 3)
        self.stack.pop()
        self.assertEqual(len(self.stack.elements), 2)
        self.stack.pop()
        self.assertEqual(len(self.stack.elements), 1)
        self.assertEqual(self.stack.pop().data, self.node_10.data)
        self.assertEqual(len(self.stack.elements), 0)
        #self.assertRaises(self.stack.pop(), IndexError("В стэке нет элементов"))
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_data(self):
        self.stack.push(self.node_10.data)
        self.assertEqual(str(self.stack.top.data), "10")

