from utils.node import Node


class Queue():
    """Класс Queue реализует структуру данных очередь, в которой первым 
    удаляется элемент, который был помещен туда первым, то есть в очереди 
    реализуется принцип «первым вошел — первым вышел» (англ. first-in, 
    first-out — FIFO). У очереди имеется голова (англ. head) и хвост 
    (англ. tail). Когда элемент ставится в очередь, он занимает место в её 
    хвосте. Из очереди всегда выводится элемент, который находится в ее голове.
    **Основные методы:**

- enqueue: добавить элемент в конец очереди
- dequeue: удалить элемент из начала очереди  """


    def __init__(self, head=None, tail=None) -> None:
        """Инициализация очереди. Для пустой - начало и конец None"""
        self.elements = []
        self.head = head
        self.tail = tail


    def enqueue(self, data) -> None:
        """ Метод добавления элемента в конец очереди"""
        if len(self.elements) == 0:
            new_node = Node(data)
            self.tail = new_node
            self.head = new_node
        elif len(self.elements) == 1:
            new_node = Node(data)
            self.head.next_node = self.tail
            self.tail = new_node
        elif len(self.elements) == 2:
            new_node = Node(data)
            self.head.next_node = self.elements[1]
            self.tail = new_node           
        else:
            new_node = Node(data)
            self.tail = new_node
            #self.elements[len(self.elements) - 1].next_data =new_node
            # self.head = Node(self.elements[len(self.elements) - 1].data, new_node)
        self.elements.append(new_node)


    def dequeue(self) -> Node: 
        """ Метод удаления элемента из начала очереди. 
        Возвращает удаленный элемент"""
        if len(self.elements) == 0:
            raise IndexError("В очереди нет элементов")
        elif len(self.elements) == 1:
            # после удаления не будет ни одного элемента
            first_node = self.head
            self.head = None
            self.tail = None
            self.elements.pop(0)
            return first_node
        else:
            # после удаления будет хотя бы один элемент
            first_node = self.head
            self.elements.pop(0)
            self.head = self.elements
            return first_node
