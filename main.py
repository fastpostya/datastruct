from utils.stack import Stack
from utils.node import Node
from utils.custom_queue import Queue
from utils.linked_list import LinkedList


def main():
    # Задание 1
    # print("Добавление")
    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # print(n2.next_node)
    # stack = Stack()
    # stack.push('data1')
    # stack.push('data2')
    # stack.push('data3')
    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)
    # print(stack.top.next_node.next_node.next_node)
    ##print(stack.top.next_node.next_node.next_node.data)
    # stack = Stack()
    # stack.push('data1')
    # data = stack.pop()
    # # стэк стал пустой
    # print(stack.top)
    # pop() удаляет элемент и возвращает данные удаленного элемента
    # print(data)
    # 'data1'
    # print(f"\nУдаление")
    # stack1 = Stack()
    # stack1.push('data4')
    # stack1.push('data5')
    # stack1.push('data6')
    # print(stack1.elements)
    # data = stack1.pop()
    # print(stack1.elements)
    # data = stack1.pop()
    # # теперь последний элемент содержит данные data4
    # print(stack1.top.data)
    # # удаление элемента из пустого стэка
    # # data = stack1.pop()

    # Задание 3
    # print("Очередь. Добавление.")
    # queue = Queue()
    # queue.enqueue('data1')
    # queue.enqueue('data2')
    # queue.enqueue('data3')
    # queue.enqueue('data4')
    # print(queue.head.data)
    # print(queue.head.next_node.data)
    # print(queue.tail.data)
    # print(queue.tail.next_node)
    # #print(queue.tail.next_node.data)
    # # Задание 4
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())

    #Задание 5
    print("Связанный список")
    ll = LinkedList()
    ll.print_ll()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()


if __name__ == "__main__":
    main()
