from utils.node import Node


class Stack():
    """
    Стэк (Stack) — структура данных, представляющая из себя упорядоченный 
    набор элементов, в которой добавление новых элементов и удаление 
    существующих производится с одного конца, называемого вершиной стека. 
    Притом первым из стека удаляется элемент, который был помещен туда последним, 
    то есть в стеке реализуется стратегия «последним вошел — первым вышел» 
    (last-in, first-out — LIFO).
    """
    def __init__(self):
        """инициализация пустого стэка"""
        self.elements = []
        #top— индекс последнего помещенного в стек элемента
        self.top = None

    def push(self, data):
        """добавление элемента"""
        new_node = Node(data)
        if len(self.elements) == 0:
            self.top = 1
        elif len(self.elements) > 1:
            self.top += 1
        elif len(self.elements) > 2:
            self.elements[len(self.elements) - 1].next = id(new_node)
            self.top += 1
        self.elements.append(new_node)
        

    def pop(self):
        """удаление элемента"""
        if len(self.elements) > 0:
            self.elements.pop(len(self.elements) - 1)
    
    #def next_node(self):
        """возвращает адрес элемента"""
        #pass