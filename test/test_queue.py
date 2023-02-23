import unittest
from utils.custom_queue import Queue
from utils.node import Node


class Test_Queue(unittest.TestCase):
    def test__init__(self):
        queue = Queue()
        self.assertEqual(queue.elements, [])
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_enqueue(self):
        node_10 = Node("10")
        node_20 = Node(20)
        node_30 = Node(30)
        node_40 = Node(40)
        queue = Queue()
        queue.enqueue(node_10)
        queue.enqueue(node_20)
        queue.enqueue(node_30)
        queue.enqueue(node_40)
        self.assertEqual(len(queue.elements), 4)

    def test_dequeue(self):
        node_10 = Node("10")
        node_20 = Node(20)
        node_30 = Node(30)
        node_40 = Node(40)
        queue = Queue()
        queue.enqueue(node_10)
        queue.enqueue(node_20)
        queue.enqueue(node_30)
        queue.enqueue(node_40)
        self.assertEqual(len(queue.elements), 4)
        #self.assertEqual(queue.head.data, node_10.data)
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(len(queue.elements), 2)
        #self.assertEqual(queue.dequeue(), node_40)
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(len(queue.elements), 0)
