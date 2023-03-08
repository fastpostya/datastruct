class Node():
    """Класс узла Node, содержащий два атрибута:
    - data - данные (любые полезные данные: число, строка, список и т.д.)
    - nexе_node - ссылка на следующий узел

    Методы:

    - __init__(self) - иницализация класса. Создаются атрибуты:
    data: данные (любой объект)
    и next_node : указатель на следующий узел

    - __repr__(self) -> str: возвращает текстовое представление объекта Node

    - next_node(self) -> Node: возвращает указатель на следующий элемент
    """
    def __init__(self, data, next_node=None) -> None:
        """инициализация пустого узла"""
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        """представление экземпляра класса Node
        возвращает только данные data
        полное представление закомментировано для последущей реализации
        """
        text = ""
        for item in self.__dict__:
            text += f'Node({str(item)}={self.__dict__[item]}), '
        text = text[:-2]
        # return f"Node(self.data)"
        return text

