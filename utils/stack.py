from utils.node import Node


class Stack():
    """
    класс Stack реализует структуру данных, представляющую стэк - упорядоченный 
    набор элементов, в которой добавление новых элементов и удаление 
    существующих производится с одного конца, называемого вершиной стека. 
    Первым из стека удаляется элемент, который был помещен туда последним, 
    то есть в стеке реализуется стратегия «последним вошел — первым вышел» 
    (last-in, first-out — LIFO).

    метод __init__(self) - иницализация класса. Создаются атрибуты 
    elements-> list: для хранения объектов класса Node
     и top ->: Node указатель на последний элемент стэка

    метод push(self, data) -> Node - добавляет в стэк элемент в виде узла 
    и возвращает объект Node, содержащий data

    метод pop(self) -> Node - удаляет последний элемент из в стэка 
    и возвращает его данные

    метод data(self) -> object - возвращает объект data, хранящийся в узле Node
    """
    def __init__(self) -> None:
        """инициализация пустого стэка"""
        self.elements = []
        # top— последний помещенный в стек элемент
        self.top = None

    def push(self, data) -> Node:
        """функция добавляет элемент в  стэк и возвращает его"""
        if len(self.elements) == 0:
            new_node = Node(data)
        else:
            new_node = Node(data, self.top)
        self.top = new_node
        return self.elements.append(new_node)

    def pop(self) -> Node:
        """функция удаляет последний элемент из стэка 
        и возвращает его данные"""
        if len(self.elements) == 0:
            raise IndexError("В стэке нет элементов")
        elif len(self.elements) == 1:
            last_node = self.top
            self.elements.pop()
            self.top = None
            return last_node.data
        elif len(self.elements) > 1:
            last_node = self.top
            self.top = self.elements[len(self.elements) - 2]
            self.elements.pop()
            return last_node.data
        else:
            self.top = None
            return None
