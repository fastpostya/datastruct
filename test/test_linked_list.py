import unittest
from io import StringIO
from contextlib import redirect_stdout
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
        # пустой связанный список
        self.empty_ll = LinkedList()
        # связанный список, который будет заполняться
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
        expected_output = "None"
        f = StringIO()
        with redirect_stdout(f):
            self.empty_ll.print_ll()
        self.assertEqual(f.getvalue().strip(), expected_output)

    def test_print_ll_multiple_elements(self):
        """тестирование метода print_ll с непустым списком"""
        self.full_ll.insert_beginning(self.node_0.data)
        self.full_ll.insert_beginning(self.node_1.data)
        self.full_ll.insert_beginning(self.node_2.data)
        self.full_ll.insert_beginning(self.node_3.data)
        expected_output = "{'id': 3} -> {'id': 2} -> {'id': 1} -> {'id': 0} -> None"
        f = StringIO()
        with redirect_stdout(f):
            self.full_ll.print_ll()
        self.assertEqual(f.getvalue().strip(), expected_output)

    def test_to_list(self) -> list:
        """Тестирование to_list, должен вернуть все поля data элементов"""
        self.full_ll.insert_at_end(self.node_0.data)
        self.full_ll.insert_at_end(self.node_1.data)
        self.full_ll.insert_at_end(self.node_2.data)
        self.full_ll.insert_at_end(self.node_3.data)
        self.assertEqual(self.full_ll.to_list(), [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}])

    def test_get_data_by_id(self):
        self.full_ll.insert_at_end(self.node_0.data)
        self.full_ll.insert_at_end(self.node_1.data)
        self.full_ll.insert_at_end(self.node_2.data)
        self.full_ll.insert_at_end(self.node_3.data)
        self.assertEqual(self.full_ll.get_data_by_id(3), {'id': 3})

    def test_get_data_by_id_not_dict(self):
        """Проверка случая, когда данные не являются словарем"""
        self.full_ll.insert_at_end("text")

        # связанный список из одного элемента
        with self.assertRaises(TypeError):
            self.full_ll.get_data_by_id(5)

        # больше одного элемента
        self.full_ll.insert_beginning(self.node_1.data)
        with self.assertRaises(TypeError):
            self.full_ll.get_data_by_id(5)

    def test_get_data_by_id_not_id(self):
        """проверка случая, когда в словаре нет ключа id"""
        self.full_ll.insert_at_end({'test': 3})

        # связанный список из одного элемента
        with self.assertRaises(KeyError):
            self.full_ll.get_data_by_id(6)
        self.full_ll.insert_beginning(self.node_1.data)

        # больше одного элемента
        with self.assertRaises(KeyError):
            self.full_ll.get_data_by_id(6)

    def test_get_data_by_id_empty(self):
        """Поиск в пустом списке несуществующего значения"""
        self.assertIsNone(self.empty_ll.get_data_by_id(7))

    def test_get_data_by_id_not_empty(self):
        """Поиск в непустом списке несуществующего значения"""
        self.full_ll.insert_at_end(self.node_0.data)
        self.full_ll.insert_at_end(self.node_1.data)
        self.full_ll.insert_at_end(self.node_2.data)
        self.full_ll.insert_at_end(self.node_3.data)
        self.assertIsNone(self.full_ll.get_data_by_id(7))