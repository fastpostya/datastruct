from utils.node import Node


class LinkedList():
    """
    Класс Linked list реализует структуру односвязного списка.
    Это линейная структура данных, включающая ряд связанных узлов. 
    Узел хранит полезные данные и адрес следующего узла. 
    Узел реализован отдельным классом Node, содержащим атрибуты 
    под данные (data) и следующий узел (next).

    Методы:
    __init__ - инициализация пустого списка.
    - insert_beginning - принимает данные (словарь) и добавляет 
    узел с этими данными в начало связанного списка
    - insert_at_end - принимает данные (словарь) и добавляет 
    узел с этими данными в конец связанного списка
    - print_ll -выводит на печать содержимое связанного списка
    """

    def __init__(self, data=None):
        """инициализация пустого списка.
        Атрибуты:
        -head: Node|None - указатель на первый элемент связанного списка,
        -tail: Node|None - указатель на последний элемент связанного списка"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data) -> None:
        """принимает данные (словарь) и добавляет узел с этими данными 
        в начало связанного списка"""
        new_node = Node(data)
        if self.head is None and self.tail is None:
            # Нет ни одного элемента
            self.tail = new_node
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data) -> None:
        """принимает данные (словарь) и добавляет узел с этими данными 
        в конец связанного списка"""
        new_node = Node(data)
        if self.head is None and self.tail is None:
            # Нет ни одного элемента
            self.head = new_node
        else: 
            self.tail.next_node = new_node       
        self.tail = new_node

    def print_ll(self) -> None:
        """Выводит на печать содержимое связанного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)
