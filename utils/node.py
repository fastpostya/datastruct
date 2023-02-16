class Node():
    """Класс узла `Node`, содержащий два атрибута:
    - данные (любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        text = ""
        for item in self.__dict__:
            text += f'{str(item)}:[{self.__dict__[item]}], '
        return text[:-2]
