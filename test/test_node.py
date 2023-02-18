import unittest
#import pytest
from utils.node import Node


# @pytest.fixture
# def node_10():
#     return Node(10)


# @pytest.fixture
# def node_20():
#     Node(20).next_node = node_10
#     return Node(20)


class Test_Node(unittest.TestCase):
    def SetUp(self):
        self.node_10= Node(10)

    def test_node__init__(self, node_10):
        self.assertEqual(Node(10), node_10)

    def test__repr__(self, node_10):
        self.assertEqual(Node(10), 10)

    def test_next_node(self, node_10, node_20):
        self.assertEqual(node_20, node_10)
