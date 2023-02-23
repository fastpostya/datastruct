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
        node_10 = Node(10)
        node_20 = Node(20)
        node_30 = Node(30)
        queue = Queue()
        queue.enqueue(node_10)
        self.assertEqual(queue.head.data,node_10.data)
        self.assertEqual(queue.tail.data,node_10.data)
        queue.enqueue(node_20)
        self.assertEqual(queue.head.data,node_10.data)
        self.assertEqual(queue.tail.data,node_20.data)  
        queue.enqueue(node_30)    
        self.assertEqual(queue.head.data,node_10.data)
        self.assertEqual(queue.head.next_node.data,node_20.data)
        self.assertEqual(queue.tail.data,node_30.data)   
        self.assertIsNone(queue.tail.next_node.data) 

