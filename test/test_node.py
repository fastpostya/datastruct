import unittest
#import pytest
from utils.node import Node


class Test_Node(unittest.TestCase):
    def setUp(self):
        self.node_10 = Node(10)
        self.node_20 = Node(20, self.node_10)

    def test_node__init__(self):
        self.assertIs(self.node_10.data, Node(10).data)

    def test__repr__(self):
        self.assertEqual(repr(Node(10)), 'Node(data=10), Node(next_node=None)')
        self.assertEqual(repr(Node(10, Node(20))), 'Node(data=10), Node(next_node=Node(data=20), Node(next_node=None))')

    def test_next_node(self):
        self.assertEqual(self.node_20.next_node, self.node_10)
