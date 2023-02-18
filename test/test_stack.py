import unittest
import pytest
from utils.stack import Stack
from utils.node import Node


@pytest.fixture
def stack_10():
    return [node_10]


class Test_Stack(unittest.TestCase):
    def test_stack__init__(self, node_10):
        self.assertEqual(Node(10), node_10)

    # def test__repr__(self, node_10):
    #     self.assertEqual(Node(10), 10)

    # def test_next_node(self, node_10, node_20):
    #     self.assertEqual(node_20, node_10)