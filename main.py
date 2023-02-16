from utils.stack import Stack
from utils.node import Node


def main():
    n1 = Node(5, None)
    print(n1)

# Результаты вывода в консоли
#5
#a
#<__main__.Node object at 0x0000022803036050>
#<__main__.Node object at 0x0000022803036050>

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    #print(stack.top.data)
    #print(stack.top.next_node.data)
    #print(stack.top.next_node.next_node.data)
    #print(stack.top.next_node.next_node.next_node)
    #print(stack.top.next_node.next_node.next_node.data)
  # Результаты вывода в консоли
  #data3
  #data2
  #data1
  #None
  #Traceback (most recent call last):
    #File "-//-//-", line 29, in <module>
      #print(stack.top.next_node.next_node.next_node.data)
  #          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  #AttributeError: 'NoneType' object has no attribute 'data'


if __name__ == "__main__":
    main()

