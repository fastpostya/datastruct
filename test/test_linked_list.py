import unittest
from utils.node import Node
from utils.linked_list import LinkedList


class Test_ll__init__(unittest.TestCase):
    """Класс Test_ll__init_ создан для тестирования класса LinkedList
    """
    def setUp(self):
        """Метод для создания объектов, используемых для тестирования"""
        self.node_0 = Node({'id': 0})
        self.node_1 = Node({'id': 1})
        self.node_2 = Node({'id': 2})
        self.node_3 = Node({'id': 3})
        self.empty_ll = LinkedList()
        self.full_ll = LinkedList()

    def test_ll__init__(self):
        """тестирование метода __init__"""
        self.assertIsNone(self.empty_ll.head)
        self.assertIsNone(self.empty_ll.tail)

    def test_insert_at_end(self):
        """тестирование метода insert_at_end"""
        self.full_ll.insert_at_end(self.node_0.data)
        self.full_ll.insert_at_end(self.node_1.data)
        self.full_ll.insert_at_end(self.node_2.data)
        self.full_ll.insert_at_end(self.node_3.data)
        self.assertEqual(self.full_ll.head.data, self.node_0.data)
        self.assertEqual(self.full_ll.tail.data, self.node_3.data)

    def test_insert_beginning(self):
        """тестирование метода insert_beginning"""
        self.full_ll.insert_beginning(self.node_0.data)
        self.full_ll.insert_beginning(self.node_1.data)
        self.full_ll.insert_beginning(self.node_2.data)
        self.full_ll.insert_beginning(self.node_3.data)
        self.assertEqual(self.full_ll.head.data, self.node_3.data)
        self.assertEqual(self.full_ll.tail.data, self.node_0.data)

    def test_print_ll_none(self):
        """тестирование метода print_ll с пустым списком"""
        expected_output = " -> None"
        self.assertIsNone(self.empty_ll.print_ll())

    def test_print_ll_multiple_elements(self):
        """тестирование метода print_ll с непустым списком"""
        self.full_ll = LinkedList()
        self.full_ll.insert_beginning(self.node_0.data)
        self.full_ll.insert_beginning(self.node_1.data)
        self.full_ll.insert_beginning(self.node_2.data)
        self.full_ll.insert_beginning(self.node_3.data)
        expected_output = "{'id': 3} -> {'id': 2} -> {'id': 1} -> {'id': 0} -> None"
        
        with captured_output() as (out, err):
            self.full_ll.print_ll()
        self.assertEqual(out.strip(), expected_output)
        


