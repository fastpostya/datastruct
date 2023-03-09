from utils.node import Node


class LinkedList():
    """
    Класс Linked list реализует структуру односвязного списка.
    Это линейная структура данных, включающая ряд связанных узлов. 
    Узел хранит полезные данные и адрес следующего узла. 
    Узел реализован отдельным классом Node, содержащим атрибуты 
    под данные (data) и следующий узел (next).
    Атрибуты:
    -date_list:list - список, содержащий поле data всех узлов 
    односвязного списка. 
    -head: Node|None - указатель на первый элемент связанного списка,
    -tail: Node|None - указатель на последний элемент связанного списка

    Методы:
    __init__ - инициализация пустого списка.
    - insert_beginning - принимает данные (словарь) и добавляет 
    узел с этими данными в начало связанного списка
    - insert_at_end - принимает данные (словарь) и добавляет 
    узел с этими данными в конец связанного списка
    - print_ll -выводит на печать содержимое связанного списка
    -get_data_by_id- метод  возвращает первый найденный в LinkedList 
        словарь с ключом id, значение которого равно переданному 
        в метод значению. 
        В случае, если data не является словарем, выбрасывается 
        исключение TypeError, если в словаре нет ключа id- KeyError.
    - to_list - возвращает список с данными, содержащимися в односвязном 
    списке LinkedList
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
        # if node is None:
        #     print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)

    def to_list(self) -> list:
        """
        возвращает список с данными, содержащимися в 
        односвязном списке LinkedList
        """
        date_list = []
        current = self.head
        while self.head.next_node:
            date_list.append(current.data)
            if current.next_node:
                current = current.next_node
            else:
                break
        return date_list

    def get_data_by_id(self, id) -> dict | TypeError:
        """ метод  возвращает первый найденный в LinkedList 
        словарь с ключом id, значение которого равно переданному 
        в метод значению. 
        В случае, если data не является словарем, выбрасывается 
        исключение TypeError, если в словаре нет ключа id- KeyError.
        """
        current = self.head
        while current:
            # if isinstance(current.data, dict) and "id" in current.data 
            # and current.data["id"] == id:
            if not isinstance(current.data, dict):
                raise TypeError("Данные не являются словарем")
            elif "id" not in current.data:
                raise KeyError("Словарь не содержит ключа id")
            else:
                if current.data["id"] == id:
                    return current.data
                else:
                    if current.next_node:
                        current = current.next_node
                    else:
                        # дошли до последнего узла в списке
                        raise IndexError(f"Словарь с ключем id={id} не найден")
                        break
        else:
            raise IndexError(f"Словарь с ключем id={id} не найден")
